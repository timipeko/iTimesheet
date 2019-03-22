from django.shortcuts import render
from django.views import generic

# Create your views here.

from timesheet.models import Customer, Project, Entry

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    entries = Entry.objects.count()

    # The 'all()' is implied by default.    
    customers = Customer.objects.count()
    
    context = {
        'num_entries': entries,
        'num_customers': customers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class EntryListView(generic.ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.all()