from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed

from .forms import CreateNewNoteForm, CreateNewNoteForm2, DeleteNoteForm
from .models import Note, Category


# Create your views here.
def index(request):
    return render(request, 'main_page.html')


def notes(request):
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST)
        if form.is_valid():
            note_to_delete = form.cleaned_data['note']
            note_to_delete.delete()
            return redirect('notes')
    elif request.method == 'GET':
        form = DeleteNoteForm()
        data = Note.objects.all()
        return render(request, 'notes_page.html', {'notes': data, 'form': form})


def create_new_note(request):
    if request.method == 'POST':
        form = CreateNewNoteForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    elif request.method == 'GET':
        form = CreateNewNoteForm2()
        return render(request, template_name='create_new_notes.html', context={'form': form})
    return HttpResponseNotAllowed(('POST', 'GET'))
