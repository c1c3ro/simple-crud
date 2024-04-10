from django.db import models
from django.urls import reverse

# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=150)
    altura = models.DecimalField(decimal_places=2, max_digits=5)
    peso = models.DecimalField(decimal_places=3, max_digits=5)
    cor = models.CharField(max_length=20)
    descricao = models.TextField(blank=True, null=True)
    possui_os_20_dedos = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('person:detail_person', kwargs={"id": self.id})