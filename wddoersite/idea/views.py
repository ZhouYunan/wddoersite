# coding:utf-8
from django.views.generic import ListView, DetailView
from wddoersite.idea.models import Idea


class IdeaIndexView(ListView):
    model = Idea
    template_name = 'idea/idea_index.html'

    def get_context_data(self, **kwargs):
        context = super(IdeaIndexView, self).get_context_data(**kwargs)

        context["amount_ideas"] = Idea.objects.all().count()
        context["ideas"] = Idea.objects.filter(is_displayed=True, tag__in=["DSBJ", "GSZS", "BCSJ"])

        return context


class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'idea/idea_detail.html'

    def get_context_data(self, **kwargs):
        context = super(IdeaDetailView, self).get_context_data(**kwargs)
        return context
