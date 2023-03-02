import os.path

from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404
from .models import files
from django.http import FileResponse
from django.utils.encoding import smart_str
from pdf2docx import Converter
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.

def get_file(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        file = files(file=file)
        file.save()
        print(file.file)
        co = Converter("media/"+str(file.file))
        co.convert('DOCX files/do.docx')
        co.close()

        response = FileResponse(open(os.path.join(BASE_DIR,'DOCX files/do.docx'),'rb'),content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('file.docx')
        return response
    return render(request,'upload.html')




