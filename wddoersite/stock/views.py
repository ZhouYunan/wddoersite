# coding:utf-8
from django.views.generic import TemplateView


class StockIndexView(TemplateView):
    template_name = "stock/stock_index.html"


class RealTimeDataView(TemplateView):
    template_name = "stock/real_time_date.html"