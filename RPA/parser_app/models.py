from django.db import models

class myuploadfiles(models.Model):
    myfiles = models.FileField(upload_to="")