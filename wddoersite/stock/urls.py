# coding:utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'stock/$', views.StockIndexView.as_view(), name="stock_index"),
    url(r'real-time/$', views.RealTimeDataView.as_view(), name="real-time"),
]