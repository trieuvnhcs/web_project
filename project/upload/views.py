from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from project.upload.models import Document
from project.upload.forms import DocumentForm


def home(request):
    return render(request, 'upload/home.html', )


def all_files(request):
    documents = Document.objects.all()
    return render(request, 'upload/all_files.html', { 'documents': documents })


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_files')
    else:
        form = DocumentForm()
    return render(request, 'upload/model_form_upload.html', {
        'form': form
    })

def login(request):
    return render(request, 'upload/login.html',)

def register(request):
    return render(request, 'upload/register.html',)

def report(request):
    documents = Document.objects.all()
    return render(request, 'upload/report.html', { 'documents': documents })
