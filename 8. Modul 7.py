"""
1. Membuat Form
2. Buat App baru dengan command prompt dengan code :

manage.py startapp tamu

3. Buka settings.py pada folder project, tambahkan ‘tamu’ pada INSTALLED_APPS.  code :

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about',
    'buku',
    'tamu',
]

4. Buat file baru dengan nama models.py pada app tamu dan isi code dengan :

from django import models

class Tamu(models.Form):
    nim = models.CharField(max_length=10)
    nama = models. CharField(max_length=10)
    kegiatan = models.CharField(
        widget = models.Textarea
    )

5. Buka file views.py pada app tamu ketik code :

from django.shortcuts import render

from . models import Post

def index(request):
    buku_tamu = Tamu()

    context = {
        'BukuTamu':buku_tamu,
    }

    return render(request, 'tamu/index.html', context)

6. Buka file urls.py pada folder project, tambahkan kode :


from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', views.index),
    path('about/', include('about.urls')),
    path('buku/', include('buku.urls')),
    path('tamu/', include('tamu.urls')),
]

7. Tambahkan file baru dengan nama urls.py pada app tamu. Ketik kode :

from.django.conf.urls import url

from . import views

urlpatterns = [
    path('/', views.index),
]

8. Tambahkan link untuk Buku Tamu pada file index.html Halaman Utama :

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOME</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    
    <img src="{% static 'img/home.jpg %}" alt="">
    <h2>Halaman Utama</h2>
    <ul>

        <li><a href="/">Home</a></li>
        <li><a href="about/">About</a></li>
        <li><a href="buku/">Data Buku</a></li>
        <li><a href="tamu/">Buku Tamu</a></li>
    </ul>
</body>
</html>

9. Tambahkan link untuk Buku Tamu pada file index.html Halaman Data Buku :

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOME</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    
    <img src="{% static 'img/home.jpg %}" alt="">
    <h2>Halaman Utama</h2>
    <ul>

        <li><a href="/">Home</a></li>
        <li><a href="about/">About</a></li>
        <li><a href="buku/">Data Buku</a></li>
        <li><a href="tamu/">Buku Tamu</a></li>
    </ul>
</body>
</html>

10. Tambahkan link untuk Buku Tamu pada file index.html Halaman About :

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOME</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    
    <img src="{% static 'img/home.jpg %}" alt="">
    <h2>Halaman Utama</h2>
    <ul>

        <li><a href="/">Home</a></li>
        <li><a href="about/">About</a></li>
        <li><a href="buku/">Data Buku</a></li>
        <li><a href="tamu/">Buku Tamu</a></li>
    </ul>
</body>
</html>

11. Buat folder baru pada app tamu dengan nama templates dan tamu
12. Buka file models.py pada app tamu dan ketik kode :

from django import models

class Tamu(models.Form):
    nim = models.CharField(max_length=10)
    nama = models. CharField(max_length=50)
    kegiatan = models.CharField(
    
    def __str__(self):
        return self.nim

13. Buka file admin.py pada app tamu dan ketik kode :

from django.contrib import admin

from . models import Guest

admin.site.register(Guest)

14. Buka cmd ketik kode :

manage.py makemigrations

15. jika sudah ketika lagi :

manage.py makemigrate 

16. Buka kembali views.py pada app tamu ketik kode :

from django.shortcuts import render

from . forms import Tamu

from . models import Guest

def index(request):
    buku_tamu = Tamu()

    context = {
        'BukuTamu':buku_tamu,
    }

    if request.method == "POST":
        Guest.objects.create(
            nim = request.POST.get('nim'),
            nama = request.POST.get('nama'),
            kegiatan = request.POST.get('kegiatan'),
        )
    
    return render(request, 'tamu/index.html', context)

17. Buka file admin.py pada app tamu, tambahkan kode :

from django.contrib import admin

from . models import Guest

class TampilanGuest(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'kegiatan')
    list_display_links = (None)
    search_fields = ('nim', 'nama')

admin.site.register(Guest, TampilGuest)

"""