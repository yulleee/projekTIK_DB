
from django.shortcuts import render

# Create your views here.
def prodi6(request):
    judul = ["Agribisnis", "Agroekoteknologi", "Ilmu Perikanan", "Teknologi Pangan"] 


    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfp.html', konteks)
