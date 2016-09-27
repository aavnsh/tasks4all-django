from django import forms
from django.forms import ModelForm

from tasklist.models import Item


class AddItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddItemForm, self).__init__(*args, **kwargs)

    due_date = forms.DateField(
        required=False,
        widget=forms.DateTimeInput(attrs={'class': 'due_date_picker'})
    )

    title = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'size': 35})
    )

    note = forms.CharField(widget=forms.Textarea(), required=False)

    class Meta:
        model = Item
        exclude = []


class EditItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditItemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Item
        exclude = ('created_date', 'created_by',)
