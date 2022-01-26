from django.shortcuts import render,HttpResponse
from .models import myuploadfiles
from pyresparser import ResumeParser
from django.conf import settings
import os

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
            resume.company_name      = data.get('company_names')
            resume.college_name       = data.get('college_name')
            l = []
            if data.get('designation'):
                for i in data.get('designation'):
                    if '@' in i:
                        continue
                    else:
                        l.append(i)

            resume.designation        = l
            resume.total_experience   = data.get('total_experience')  

            if data.get('skills') is not None:
                resume.skills         = ', '.join(data.get('skills'))
            else:
                resume.skills         = None 
            
            if data.get('degree') is not None:
                resume.education      = ', '.join(data.get('degree'))
            else:
                resume.education      = None
            
            if data.get('experience') is not None:
                resume.experience     = ', '.join(data.get('experience'))
            else:
                resume.experience     = None
            
            resume.save()
            resumes = myuploadfiles.objects.all()
            context = {
                'resumes': resumes,
            }
            

           

        return render(request,'UI.html',context)
        #return HttpResponse("Files Uploaded Successfully")