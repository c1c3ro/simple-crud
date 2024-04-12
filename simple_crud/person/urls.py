from django.urls import path
from .views import PersonCreateView, PersonListView, PersonDetailView, PersonUpdateView, PersonDeleteView


app_name = "person"

urlpatterns = [
    path('list/', PersonListView.as_view(), name='list_person'),
    path('create/', PersonCreateView.as_view(), name='create_person'),
    path('detail/<int:id>/', PersonDetailView.as_view(), name='detail_person'),
    path('update/<int:id>/', PersonUpdateView.as_view(), name='update_person'),
    path('delete/<int:id>/', PersonDeleteView.as_view(), name='delete_person'),
]
