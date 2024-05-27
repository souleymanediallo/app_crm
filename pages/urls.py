from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import dashboard_view

urlpatterns = [
    path("", views.home, name="home"),
    path('', view=dashboard_view, name="dashboard"),

]