from django import forms
from django.forms import widgets

statuses = [('new', 'Новая'), ('in process', 'В процессе'),
            ('ready', 'Сделано')]


class TodoForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description',
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'Введите название',
                                             'type': 'text', 'class': 'form-control'}))
    status = forms.CharField(max_length=15, required=True, label='Status',
                             widget=forms.Select(choices=statuses, attrs={'class': "form-control"}))
    deadline = forms.DateField(required=True, label='Deadline', widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    more_info = forms.CharField(max_length=200, required=False, label='More Info',
                                widget=forms.Textarea(
                                    attrs={'placeholder': 'Введите описание', 'class': 'form-control'}))
