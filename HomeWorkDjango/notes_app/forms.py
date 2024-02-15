from django import forms

from .models import Category, Note


class CreateNewNoteForm(forms.Form):
    title=forms.CharField(max_length=255)
    text=forms.CharField(widget=forms.Textarea)
    reminder = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ModelChoiceField(queryset=Category.objects)

class CreateNewNoteForm2(forms.ModelForm):
    reminder = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class DeleteNoteForm(forms.Form):
    note = forms.ModelChoiceField(queryset=Note.objects, label='Видалити нотатку:')