from django.views.generic import CreateView, DetailView, ListView

from .models import Workstation


class WorkstationListView(ListView):
    model = Workstation


class WorkstationDetailView(DetailView):
    model = Workstation


class WorkstationCreateView(CreateView):
    model = Workstation
    fields = [
        "w_name",
        "belarc_file",
        "anti_virus",
        "os_build",
        "installed",
        "network_speed",
        "is_installed",
    ]
