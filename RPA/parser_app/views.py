from django.shortcuts import render,HttpResponse
from . models import myuploadfiles

def index(request):
    return render(request,"index.html")

def send_files(request):
    if request.method == "POST":
        myfile = request.FILES.getlist("UploadFiles")

        for f in myfile:
            myuploadfiles(myfiles = f).save()

        return HttpResponse("Files Uploaded Successfully")