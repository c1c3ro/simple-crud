from django.urls import path
from .views import PersonCreateView, PersonListView, PersonDetailView


app_name = "person"

urlpatterns = [
    path('list/', PersonListView.as_view(), name='list_person'),
    path('create/', PersonCreateView.as_view(), name='create_person'),
    path('detail/<int:id>/', PersonDetailView.as_view(), name='detail_person'),
]
