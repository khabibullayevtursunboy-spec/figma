from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

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