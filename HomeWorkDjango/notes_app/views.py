from django.shortcuts import render
from django.http import HttpResponse

from .models import Note


# Create your views here.
def index(request):
    return render(request, 'main_page.html')


def notes(request):
    data = Note.objects.all()
    return render(request, 'notes_page.html', {'notes': data})
