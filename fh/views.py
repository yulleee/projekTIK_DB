from django.shortcuts import render

# Create your views here.
def prodi2(request):
    judul = ["Ilmu Hukum"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfh.html', konteks)
