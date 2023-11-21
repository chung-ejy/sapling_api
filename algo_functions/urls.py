from . import views
from django.urls import path

urlpatterns = [
    path("backtest",views.backtestView,name="backtest"),
    path("trades",views.tradesView,name="trades"),
    path("recommendations",views.recommendationsView,name="recommendations"),
    path("portfolios",views.portfoliosView,name="portfolios"),
]