# Generated by Django 2.2.4 on 2019-11-12 18:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pyc', '0004_auto_20191112_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]