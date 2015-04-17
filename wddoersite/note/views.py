from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, TemplateView, DetailView

from models import Note, Category



class IndexView(TemplateView):
    template_name = 'note/index.html'


def about(request):
    return render(request, 'note/about.html')


class NoteIndexView(ListView):
    model = Note
    template_name = 'note/indexNote.html'
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super(NoteIndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context