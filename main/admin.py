from django.contrib import admin
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

admin.site.register(Massage)
admin.site.register(Birinchisahifa)
admin.site.register(Appdownload)
admin.site.register(TeamMember)
admin.site.register(Feature)
admin.site.register(TeamGroup)
admin.site.register(TeamSectionFeature)
admin.site.register(HowItWorksStep)
admin.site.register(VideoSection)
admin.site.register(AppProblemSolution)
admin.site.register(Testimonial)
admin.site.register(PricingPlan)
admin.site.register(FooterLink)
admin.site.register(FooterSettings)