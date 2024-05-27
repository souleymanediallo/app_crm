from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required
def home(request):
    return render(request, "pages/index.html")


class DashboardView(LoginRequiredMixin, TemplateView):
    pass


dashboard_view = DashboardView.as_view(template_name="pages/index.html")


