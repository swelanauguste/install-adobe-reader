from django.urls import path

from . import views

app_name = "machines"


urlpatterns = [
    path("", views.WorkstationsListView.as_view(), name="list"),
    path(
        "<str:pk>/<slug:slug>", views.WorkstationsDetailView.as_view(), name="detail"
    ),
    path("add", views.WorkstationsCreateView.as_view(), name="create"),
]
