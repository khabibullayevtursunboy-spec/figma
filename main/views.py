# tasks_demo/views.py
import os
from django.core.cache import cache
from django.core.files.storage import default_storage
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import *
from .serializers import *


CACHE_TTL = 60 * 10


class BaseCachedListCreateAPIView(ListCreateAPIView):
    @property
    def cache_prefix(self):
        return self.__class__.__name__

    def list(self, request, *args, **kwargs):
        query_string = request.META.get('QUERY_STRING', '')
        key = f"{self.cache_prefix}:list:{query_string}"

        cached_data = cache.get(key)

        if cached_data is not None:
            return Response(
                {
                    "success": True,
                    "message": "get ishladi (cache)",
                    "data": cached_data,
                },
                status=status.HTTP_200_OK,
            )

        response = super().list(request, *args, **kwargs)
        data_to_cache = response.data

        cache.set(key, data_to_cache, timeout=CACHE_TTL)

        return Response(
            {
                "success": True,
                "message": "get ishladi",
                "data": data_to_cache,
            },
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        keys_pattern = f"{self.cache_prefix}:list:*"
        if hasattr(cache, 'delete_pattern'):
            cache.delete_pattern(keys_pattern)
        else:
            query_string = request.META.get('QUERY_STRING', '')
            key = f"{self.cache_prefix}:list:{query_string}"
            cache.delete(key)

        return Response(
            {
                "success": True,
                "message": "created successfully",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


# --- Figma Modellariga tegishli Viewlar ---

class MassageListView(BaseCachedListCreateAPIView):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer


class BirinchisahifaListView(BaseCachedListCreateAPIView):
    queryset = Birinchisahifa.objects.all()
    serializer_class = BirinchisahifaSerializer


class AppdownloadListView(BaseCachedListCreateAPIView):
    queryset = Appdownload.objects.all()
    serializer_class = AppdownloadSerializer


class TeamMemberListView(BaseCachedListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class FeatureListView(BaseCachedListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class TeamGroupListView(BaseCachedListCreateAPIView):
    queryset = TeamGroup.objects.all()
    serializer_class = TeamGroupSerializer


class TeamSectionFeatureListView(BaseCachedListCreateAPIView):
    queryset = TeamSectionFeature.objects.all()
    serializer_class = TeamSectionFeatureSerializer


class HowItWorksStepListView(BaseCachedListCreateAPIView):
    queryset = HowItWorksStep.objects.all()
    serializer_class = HowItWorksStepSerializer


class VideoSectionListView(BaseCachedListCreateAPIView):
    queryset = VideoSection.objects.all()
    serializer_class = VideoSectionSerializer


class AppProblemSolutionListView(BaseCachedListCreateAPIView):
    queryset = AppProblemSolution.objects.all()
    serializer_class = AppProblemSolutionSerializer


class TestimonialListView(BaseCachedListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class PricingPlanListView(BaseCachedListCreateAPIView):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer


class FooterLinkListView(BaseCachedListCreateAPIView):
    queryset = FooterLink.objects.all()
    serializer_class = FooterLinkSerializer


class FooterSettingsListView(BaseCachedListCreateAPIView):
    queryset = FooterSettings.objects.all()
    serializer_class = FooterSettingsSerializer


# --- Celery Asinxron Vazifalar Uchun Viewlar ---

class AddTaskCreateView(APIView):
    def post(self, request):
        serializer = AddTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        async_result = add.delay(
            serializer.validated_data["x"],
            serializer.validated_data["y"],
        )

        return Response(
            {
                "task_id": async_result.id,
                "state": "PENDING",
                "status_url": f"/api/tasks/{async_result.id}/",
            },
            status=status.HTTP_202_ACCEPTED,
        )


class TaskStatusView(APIView):
    def get(self, request, task_id):
        return Response(build_task_status(task_id))

    def delete(self, request, task_id):
        celery_app.control.revoke(task_id, terminate=True, signal="SIGTERM")
        return Response(
            {"task_id": task_id, "state": "REVOKED"},
            status=status.HTTP_200_OK,
        )


class ImportCSVView(APIView):
    def post(self, request):
        csv_file = request.FILES.get("file")
        if not csv_file:
            return Response({"error": "Fayl topilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        file_content = csv_file.read()
        async_result = import_csv_task.delay(file_content)

        return Response(
            {
                "task_id": async_result.id,
                "status": "Import jarayoni boshlandi",
                "status_url": f"/api/tasks/{async_result.id}/",
            },
            status=status.HTTP_202_ACCEPTED,
        )


class SumRangeCreateView(APIView):
    def post(self, request):
        n = request.data.get("n", 1000000)
        async_result = sum_range.delay(n)
        return Response(
            {
                "task_id": async_result.id,
                "state": "PENDING",
                "status_url": f"/api/tasks/{async_result.id}/",
            },
            status=status.HTTP_202_ACCEPTED,
        )


class ResizeImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResizeImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image_file = serializer.validated_data["file"]
        file_path = default_storage.save(image_file.name, image_file)
        async_result = resize_image_task.delay(file_path)

        return Response(
            {
                "task_id": async_result.id,
                "state": "PENDING",
                "status_url": f"/api/tasks/{async_result.id}/",
            },
            status=status.HTTP_202_ACCEPTED,
        )


class SendEmailTaskView(APIView):
    def post(self, request):
        serializer = EmailTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_email = serializer.validated_data["email"]
        message = serializer.validated_data["message"]

        async_result = send_notification_email.delay(user_email, message)

        return Response(
            {
                "task_id": async_result.id,
                "state": "PENDING",
                "status_url": f"/api/tasks/{async_result.id}/",
            },
            status=status.HTTP_202_ACCEPTED,
        )