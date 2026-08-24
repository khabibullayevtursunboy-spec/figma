from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics

from .models import (
    Massage,
    Birinchisahifa,
    Appdownload,
    TeamMember,
    Feature,
    TeamGroup,
    TeamSectionFeature,
    HowItWorksStep,
    VideoSection,
    AppProblemSolution,
    Testimonial,
    PricingPlan,
    FooterLink,
    FooterSettings,
)
from .serializers import (
    MassageSerializer,
    BirinchisahifaSerializer,
    AppdownloadSerializer,
    TeamMemberSerializer,
    FeatureSerializer,
    TeamGroupSerializer,
    TeamSectionFeatureSerializer,
    HowItWorksStepSerializer,
    VideoSectionSerializer,
    AppProblemSolutionSerializer,
    TestimonialSerializer,
    PricingPlanSerializer,
    FooterLinkSerializer,
    FooterSettingsSerializer,
)

CACHE_TTL = 60 * 15


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class MassageListView(generics.ListAPIView):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class BirinchisahifaListView(generics.ListAPIView):
    queryset = Birinchisahifa.objects.all()
    serializer_class = BirinchisahifaSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AppdownloadListView(generics.ListAPIView):
    queryset = Appdownload.objects.all()
    serializer_class = AppdownloadSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class TeamMemberListView(generics.ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class FeatureListView(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class TeamGroupListView(generics.ListAPIView):
    queryset = TeamGroup.objects.all()
    serializer_class = TeamGroupSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class TeamSectionFeatureListView(generics.ListAPIView):
    queryset = TeamSectionFeature.objects.all()
    serializer_class = TeamSectionFeatureSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class HowItWorksStepListView(generics.ListAPIView):
    queryset = HowItWorksStep.objects.all()
    serializer_class = HowItWorksStepSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class VideoSectionListView(generics.ListAPIView):
    queryset = VideoSection.objects.all()
    serializer_class = VideoSectionSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AppProblemSolutionListView(generics.ListAPIView):
    queryset = AppProblemSolution.objects.all()
    serializer_class = AppProblemSolutionSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class PricingPlanListView(generics.ListAPIView):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class FooterLinkListView(generics.ListAPIView):
    queryset = FooterLink.objects.all()
    serializer_class = FooterLinkSerializer


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class FooterSettingsListView(generics.ListAPIView):
    queryset = FooterSettings.objects.all()
    serializer_class = FooterSettingsSerializer