from django.views.generic import CreateView, DetailView, ListView

from .models import Workstations


class WorkstationsListView(ListView):
    model = Workstations


class WorkstationsDetailView(DetailView):
    model = Workstations


class WorkstationsCreateView(CreateView):
    model = Workstations
    fields = [
        "w_name",
        "belarc_file",
        "anti_virus",
        "os_build",
        "installed",
        "network_speed",
        "is_installed",
    ]
