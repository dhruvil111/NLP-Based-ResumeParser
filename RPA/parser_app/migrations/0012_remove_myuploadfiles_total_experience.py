# Generated by Django 3.2.11 on 2022-03-14 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0011_myuploadfiles_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuploadfiles',
            name='total_experience',
        ),
    ]
