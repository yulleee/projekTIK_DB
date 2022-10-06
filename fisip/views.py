
from django.shortcuts import render

# Create your views here.
def prodi3(request):
    judul = ["Administrasi Publik", "Ilmu Komunikasi", "Ilmu Pemerintahan"] 


    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfisip.html', konteks)
