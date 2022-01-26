# Generated by Django 3.2.11 on 2022-01-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadfiles',
            name='college_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='College Name'),
        ),
        migrations.AddField(
            model_name='myuploadfiles',
            name='company_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Company Name'),
        ),
        migrations.AddField(
            model_name='myuploadfiles',
            name='designation',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Designation'),
        ),
        migrations.AddField(
            model_name='myuploadfiles',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Education'),
        ),
        migrations.AddField(
            model_name='myuploadfiles',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='myuploadfiles',
            name='experience',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Experience'),
        ),
        migrations.AddField(
            model_name='myuploadfiles',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile Number'),
        ),
        migrations.AddField(
            model_name='myuploadfiles',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='myuploadfiles',
            name='skills',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Skills'),
        ),
        migrations.AddField(
            model_name='myuploadfiles',
            name='total_experience',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Total Experience (in Years)'),
        ),
        migrations.AlterField(
            model_name='myuploadfiles',
            name='myfiles',
            field=models.FileField(upload_to='media', verbose_name='Resume'),
        ),
    ]