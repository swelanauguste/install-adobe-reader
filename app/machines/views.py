from django.views.generic import CreateView, DetailView, ListView

from .models import Belarc, Workstation


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

    def get_context_data(self, *args, **kwargs):
        context = super(WorkstationCreateView, self).get_context_data(*args, **kwargs)
        context["belarc"] = Belarc.objects.last()
        return context
