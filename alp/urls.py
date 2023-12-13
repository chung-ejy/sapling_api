from . import views
from django.urls import path

urlpatterns = [
    path("account",views.accountView,name="account"),
    path("positions",views.positionsView,name="positions"),
]