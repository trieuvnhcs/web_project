from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from project.upload.models import Document, Report
from project.upload.forms import DocumentForm,ReportForm


def home(request):
    return render(request, 'upload/home.html')

def all_files(request):
    documents = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'upload/all_files.html', { 'documents': documents })

def one_file(request, document_id):
    document = Document.objects.filter(pk=document_id)
    return render(request, 'upload/one_file.html', { 'document' : document })    

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            document = Document.objects.last()
            document_id = document.pk            
            return one_file(request,document_id)
    else:
        form = DocumentForm()
    return render(request, 'upload/model_form_upload.html', {'form': form})

def report(request, document_id):
    if request.method == "POST":  
        document = Document.objects.get(pk=document_id)        
        form = ReportForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.document = document
            new_form.save()            
            return redirect('all_files')
    else:
        document = Document.objects.get(pk=document_id)        
        form = ReportForm()       
    return render(request, 'upload/report.html', {'document':document, 'form':form})




 