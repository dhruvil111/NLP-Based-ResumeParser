# Generated by Django 3.2.11 on 2022-02-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0003_remove_myuploadfiles_college_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadfiles',
            name='college_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='College Name'),
        ),
    ]
