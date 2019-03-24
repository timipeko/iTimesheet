from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class meta:
        model = Entry
        fields=['date','customer','project','duration','description']