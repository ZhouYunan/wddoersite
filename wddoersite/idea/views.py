# coding:utf-8
from django.views.generic import ListView, DetailView
from wddoersite.idea.filters import IdeaFilter
from wddoersite.idea.models import Idea
from django_filters.views import FilterView


class IdeaIndexView(ListView):
    model = Idea
    template_name = 'idea/idea_index.html'

    def get_context_data(self, **kwargs):
        context = super(IdeaIndexView, self).get_context_data(**kwargs)

        context["amount_ideas_displayed"] = Idea.objects.all().filter(is_displayed=True, tag__in=["DSBJ", "GSZS", "BCSY"]).count()
        context["ideas"] = Idea.objects.filter(is_displayed=True, tag__in=["DSBJ", "GSZS", "BCSY"]).order_by("-created_date")

        return context


# class IdeaDetailView(DetailView):
#     model = Idea
#     template_name = 'idea/idea_detail.html'
#
#     def get_queryset(self):
#         idead = super(IdeaDetailView, self).get_queryset()
#         return idead.filter(is_displayed=True)
#
#     def get_context_data(self, **kwargs):
#         context = super(IdeaDetailView, self).get_context_data(**kwargs)
#         return context


class IdeaFilterView(FilterView):
    template_name = "idea/idea_filter.html"
    filterset_class = IdeaFilter
    queryset = Idea.objects.filter(is_displayed=True).order_by("-created_date")
