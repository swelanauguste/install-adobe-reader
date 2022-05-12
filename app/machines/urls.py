from django.urls import path

from . import views

app_name = "machines"


urlpatterns = [
    path("", views.WorkstationListView.as_view(), name="list"),
    path(
        "<str:pk>/<slug:slug>", views.WorkstationDetailView.as_view(), name="detail"
    ),
    path("add", views.WorkstationCreateView.as_view(), name="create"),
]
