
from django.shortcuts import render

# Create your views here.
def prodi4(request):
    judul = ["Kedokteran", "Keperawatan S1", "Keperawatan D3", "S1 Gizi", "Ilmu Keolahragaan"] 


    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfk.html', konteks)
