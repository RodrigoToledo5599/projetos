# Generated by Django 4.1.1 on 2022-10-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoList', '0004_alter_task_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
