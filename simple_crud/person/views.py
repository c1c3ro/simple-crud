from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView
)

from .forms import PersonForm
from .models import Person

class PersonListView(ListView):
    template_name="person_list.html"
    queryset=Person.objects.all()

class PersonDetailView(DetailView):
    template_name="person_detail.html"
    queryset=Person.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Person, id=id_)

class PersonCreateView(CreateView):
    template_name="person_create.html"
    form_class=PersonForm
    success_url="../"
    queryset=Person.objects.all()

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        "title": "This is my h1 title, did you like it?",
        "paragraph": "This is my paragraph, it came from the context, how awesome is that?",
        "my_items": ['apple', "banana", 'mango', 'pie', "eggs", 'delicious', 'fruit']
    }

    

    return render(request, "home.html", my_context)
