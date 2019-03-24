from django.shortcuts import render
from django.views import generic
from django.db.models import Sum
from extra_views import ModelFormSetView
from .forms import EntryForm

# Create your views here.

from timesheet.models import Customer, Project, Entry

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    entries = Entry.objects.count()

    # The 'all()' is implied by default.    
    hours = list(Entry.objects.aggregate(Sum('duration')).values())[0]

    customers = Customer.objects.values_list('name', flat=True) 
    
    context = {
        'num_entries': entries,
        'sum_hours': hours,
        'customers': customers
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def entry_form(request):
    return render(request, 'timesheet/entry_form.html')

class EntryListView(generic.ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

    def get_context_data(self,**kwargs):
        context = super(EntryListView,self).get_context_data(**kwargs)
        context['duration_sum'] = list(Entry.objects.filter(user=self.request.user).aggregate(Sum('duration')).values())[0]
        return context

class EntryFormSet(ModelFormSetView):
    model = Entry
    template_name = 'timesheet/entry_form.html'
    form_class = EntryForm