from . import views
from django.urls import path

urlpatterns = [
    path("account",views.accountView,name="account"),
    path("positions",views.positionsView,name="positions"),
    path("close",views.closeView,name="close"),
    path("orders",views.ordersView,name="orders"),
    path("history",views.historyView,name="history"),
]