from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from models import Note, Category
from datetime import datetime



def index(request):
    return render(request, 'note/index.html', {'current_time': datetime.now()})


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


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detailNote.html'

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def categoryIndex(request, pk):
    cate = Category.objects.get(pk=pk)
    notes = cate.note_set.all()
    return render_to_response('note/indexCategory.html',
        {
            'notes': notes,
            'cate_name': cate.name,
            'categories': Category.objects.all()
        },
        context_instance=RequestContext(request)
    )