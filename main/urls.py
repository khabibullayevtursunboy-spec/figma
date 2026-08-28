# tasks_demo/urls.py
from django.urls import path
from .views import (
    # Figma model viewlari
    MassageListView,
    BirinchisahifaListView,
    AppdownloadListView,
    TeamMemberListView,
    FeatureListView,
    TeamGroupListView,
    TeamSectionFeatureListView,
    HowItWorksStepListView,
    VideoSectionListView,
    AppProblemSolutionListView,
    TestimonialListView,
    PricingPlanListView,
    FooterLinkListView,
    FooterSettingsListView,

    # Celery task viewlari
    AddTaskCreateView,
    TaskStatusView,
    ImportCSVView,
    SumRangeCreateView,
    ResizeImageView,
    SendEmailTaskView,
)

urlpatterns = [
    # --- Figma API Endpoints (Keshlash bilan) ---
    path('messages/', MassageListView.as_view(), name='messages-list'),
    path('home/', BirinchisahifaListView.as_view(), name='home-list'),
    path('app-downloads/', AppdownloadListView.as_view(), name='app-downloads-list'),
    path('team-members/', TeamMemberListView.as_view(), name='team-members-list'),
    path('features/', FeatureListView.as_view(), name='features-list'),
    path('team-groups/', TeamGroupListView.as_view(), name='team-groups-list'),
    path('team-section-features/', TeamSectionFeatureListView.as_view(), name='team-section-features-list'),
    path('how-it-works/', HowItWorksStepListView.as_view(), name='how-it-works-list'),
    path('videos/', VideoSectionListView.as_view(), name='videos-list'),
    path('solutions/', AppProblemSolutionListView.as_view(), name='solutions-list'),
    path('testimonials/', TestimonialListView.as_view(), name='testimonials-list'),
    path('pricing/', PricingPlanListView.as_view(), name='pricing-list'),
    path('footer-links/', FooterLinkListView.as_view(), name='footer-links-list'),
    path('footer-settings/', FooterSettingsListView.as_view(), name='footer-settings-list'),

    # --- Celery Task Endpoints ---
    path('tasks/add/', AddTaskCreateView.as_view(), name='task-add'),
    path('tasks/<str:task_id>/', TaskStatusView.as_view(), name='task-status'),
    path('tasks/import-csv/', ImportCSVView.as_view(), name='task-import-csv'),
    path('tasks/sum-range/', SumRangeCreateView.as_view(), name='task-sum-range'),
    path('tasks/resize-image/', ResizeImageView.as_view(), name='task-resize-image'),
    path('tasks/send-email/', SendEmailTaskView.as_view(), name='send-email'),
]