# Generated by Django 3.2.11 on 2022-03-11 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0008_remove_myuploadfiles_exp_len'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuploadfiles',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='myuploadfiles',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='myuploadfiles',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='myuploadfiles',
            name='experience',
        ),
    ]