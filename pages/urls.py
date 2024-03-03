from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import dashboard_view, MyPasswordChangeView, MyPasswordSetView

urlpatterns = [
    path("", views.home, name="home"),
    path('', view=dashboard_view, name="dashboard"),
    path(
            "account/password/change/",
            login_required(MyPasswordChangeView.as_view()),
            name="account_change_password",
        ),
    path(
            "account/password/set/",
            login_required(MyPasswordSetView.as_view()),
            name="account_set_password",
        ),
]