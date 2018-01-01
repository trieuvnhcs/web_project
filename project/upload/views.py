from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from project.upload.models import Document, Report
from project.upload.forms import DocumentForm,ReportForm


def home(request):
    return render(request, 'upload/home.html', )


def all_files(request):
    documents = Document.objects.all()
    return render(request, 'upload/all_files.html', { 'documents': documents })

def one_file(request, document_id):
    d = Document.objects.filter(id=document_id)
    return render(request, 'upload/one_file.html', { 'd' : d })

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_files')
    else:
        form = DocumentForm()
    return render(request, 'upload/model_form_upload.html', {'form': form})

def login(request):
    return render(request, 'upload/login.html',)

def register(request):
    return render(request, 'upload/register.html',)

def report(request, document_id):
    if request.method == "POST":  
        d = Document.objects.get(pk=document_id)        
        form = ReportForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.document = d
            new_form.save()            
            return redirect('all_files')
    else:
        d = Document.objects.get(id=document_id)        
        form = ReportForm()       
    return render(request, 'upload/report.html', {'d':d, 'form':form})




 