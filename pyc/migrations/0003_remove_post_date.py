# Generated by Django 2.2.4 on 2019-11-11 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyc', '0002_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]
