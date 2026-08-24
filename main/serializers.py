from rest_framework import serializers
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


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = '__all__'


class BirinchisahifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Birinchisahifa
        fields = '__all__'


class AppdownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appdownload
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class TeamGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamGroup
        fields = '__all__'


class TeamSectionFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSectionFeature
        fields = '__all__'


class HowItWorksStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowItWorksStep
        fields = '__all__'


class VideoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSection
        fields = '__all__'


class AppProblemSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppProblemSolution
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = '__all__'


class FooterLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = '__all__'


class FooterSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSettings
        fields = '__all__'