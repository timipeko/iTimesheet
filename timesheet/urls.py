from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entries/', views.EntryListView.as_view(), name='entries'),
    path('entry_form/', views.entry_form, name='entry_form')
]