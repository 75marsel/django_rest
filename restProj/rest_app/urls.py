from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.project_view, name="project_view"),
    path("details/<int:pk>", views.get_detail_view, name="detail_view"),
]
