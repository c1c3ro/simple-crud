from typing import Any
from django.db.models.base import Model as Model
from django.urls import reverse
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView
)

from .forms import PersonForm
from .models import Person

class PersonListView(LoginRequiredMixin, ListView):
    template_name="person_list.html"
    queryset=Person.objects.all()
    

class PersonDetailView(LoginRequiredMixin, DetailView):
    template_name="person_detail.html"
    queryset=Person.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Person, id=id_)
    
class PersonDeleteView(LoginRequiredMixin, DeleteView):
    template_name="person_delete.html"
    queryset=Person.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Person, id=id_)
    
    def get_success_url(self):
        return reverse("person:list_person")

class PersonCreateView(LoginRequiredMixin, CreateView):
    template_name="person_create.html"
    form_class=PersonForm
    #success_url="../"
    queryset=Person.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class PersonUpdateView(LoginRequiredMixin, UpdateView):
    template_name="person_update.html"
    form_class=PersonForm
    #success_url="../"
    queryset=Person.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Person, id=id_)

def logout_view(request):
    logout(request)
    return render(request, "registration/logged_out.html", {})

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        "title": "This is my h1 title, did you like it?",
        "paragraph": "This is my paragraph, it came from the context, how awesome is that?",
        "my_items": ['apple', "banana", 'mango', 'pie', "eggs", 'delicious', 'fruit']
    }

    return render(request, "home.html", my_context)
