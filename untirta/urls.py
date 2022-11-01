"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from feb.views import prodi1
from fh.views import prodi2
from fisip.views import prodi3
from fk.views import prodi4
from fkip.views import prodi5
from fp.views import prodi6
from ft.views import prodi7
from pascasarjana.views import prodi8
from profil.views import profil
from mahasiswa.views import *
from dosen.views import *
from tendik.views import *
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('feb/', prodi1),
    path('fh/', prodi2),
    path('fisip/', prodi3),
    path('fk/', prodi4),
    path('fkip/', prodi5),
    path('fp/', prodi6),
    path('ft/', prodi7),
    path('pascasarjana/', prodi8),
    path('profil/', profil),
    path('mahasiswa/', mahasiswa),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name='hapus_mahasiswa'),
    path('dosen/', dosen),
    path('tambah-dosen/', tambah_dosen, name='tambah_dosen'),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),
    path('tendik/', tendik),
    path('tambah-tendik/', tambah_tendik, name='tambah_tendik'),
    path('tendik/ubah/<int:id_tendik>', ubah_tendik, name='ubah_tendik'),
    path('tendik/hapus/<int:id_tendik>', hapus_tendik, name='hapus_tendik'),
    path('', views.index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)