# Generated by Django 4.1.1 on 2022-10-03 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoList', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
    ]
