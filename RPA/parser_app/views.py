from django.shortcuts import render,HttpResponse
from .models import myuploadfiles
from RPA.resume_parser import ResumeParser
from django.conf import settings
import os
from RPA import utils 

def index(request):
    return render(request,"index.html")

def send_files(request):
    if request.method == "POST":
        myfile = request.FILES.getlist("UploadFiles")

        for f in myfile:
            #myuploadfiles(myfiles = f)
            resume = myuploadfiles(myfiles = f)
            resume.save()
            parser = ResumeParser(os.path.join(settings.MEDIA_ROOT, resume.myfiles.name))

            data = parser.get_extracted_data()
            resume.name               = data.get('name')
            resume.email              = data.get('email')
            resume.mobile_number      = data.get('mobile_number')
            #resume.company_name      = data.get('company_names')
            #resume.college_name       = data.get('college_name')

            #if data.get('designation') is not None:
             #   resume.designation     = data.get('designation')
            #else:
             #   resume.designation     = None

            resume.total_experience   = data.get('total_experience')  

            resume.skills = data.get('skills')

            resume.education      = ',\n '.join(data.get('education'))

            #if data.get('skills') is not None:
                #resume.skills         = ', '.join(data.get('skills'))
            #else:
                #resume.skills         = None 
            
            #if data.get('education') is not None:
                #resume.education      = ',\n '.join(data.get('education')) 
            #else:
                #resume.education      = None
            
            #if data.get('experience') is not None:
             #   resume.experience     = data.get('experience')
            #else:
             #   resume.experience     = None
            
            resume.experience = data.get('experience') 
            resume.summary = data.get('summary')

        
            resume.save()
            resumes = myuploadfiles.objects.all()
            context = {
                'resumes': resumes,
            }
            

           

        return render(request,'UI2.html',context)
