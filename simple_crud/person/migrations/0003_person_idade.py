# Generated by Django 5.0.4 on 2024-04-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_alter_person_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='idade',
            field=models.CharField(default='Não informado', max_length=20),
        ),
    ]