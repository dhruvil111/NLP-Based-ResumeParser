# Generated by Django 3.2.11 on 2022-03-11 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0007_myuploadfiles_exp_len'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuploadfiles',
            name='exp_len',
        ),
    ]