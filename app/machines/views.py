from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from hitcount.views import HitCountDetailView, HitCountMixin

from .models import Belarc, Workstation


class WorkstationListView(HitCountMixin, ListView):
    model = Workstation
    count_hit = True


class WorkstationDetailView(HitCountDetailView):
    model = Workstation
    count_hit = True


class WorkstationCreateView(LoginRequiredMixin, CreateView):
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
