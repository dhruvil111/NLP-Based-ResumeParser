from django.db import models
import json

class myuploadfiles(models.Model):
    myfiles = models.FileField('Resume', upload_to="media")
    name          = models.CharField('Name', max_length=255, null=True, blank=True)
    email         = models.CharField('Email', max_length=255, null=True, blank=True)
    mobile_number = models.CharField('Mobile Number',  max_length=255, null=True, blank=True)
    education     = models.CharField('Education', max_length=255, null=True, blank=True)
    skills        = models.CharField('Skills', max_length=1000, null=True, blank=True)
    #company_name  = models.CharField('Company Name', max_length=1000, null=True, blank=True)
    #college_name  = models.CharField('College Name', max_length=1000, null=True, blank=True)
    #designation   = models.CharField('Designation', max_length=1000, null=True, blank=True)
    experience    = models.CharField('Experience', max_length=1000, null=True, blank=True)
    #uploaded_on   = models.DateTimeField('Uploaded On', auto_now_add=True)
    #total_experience  = models.CharField('Total Experience (in Years)', max_length=1000, null=True, blank=True)
    summary = models.CharField('summary', max_length=1000, null=True, blank=True)
    #duration = models.CharField('Duration', max_length=255, null=True, blank=True)
    #exp_len = models.CharField('exp_len', max_length=255, null=True, blank=True)
    
    @property
    def convert_to_json(self):
        #print(json.loads(self.experience).items())
        return json.loads(self.experience).items()


        





