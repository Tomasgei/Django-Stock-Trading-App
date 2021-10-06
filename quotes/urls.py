from django.urls import path
from . import views
from . views import Signal_list_view, TradingSignal, delete
urlpatterns = [
    path("", views.home_view, name = "home_page"),                                           # function based view
    path("about.html", views.about_view, name = "about_page"),                               # function based view
    path("portfolio.html", views.portfolio_view, name = "portfolio_page"),                   # function based view
    path("market_dashboard", Signal_list_view.as_view(), name = "market_dashboard_page"),    # class based view
    path("delete/<stock_id>", views.delete, name = "delete"),                                # function based view
    path("delete_stock.html", views.delete_stock_view, name = "delete_stock"),               # function based view
]
