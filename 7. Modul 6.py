"""
1. Membuat model App
2. Pastikan Apache dan MySQL pada Xampp diaktifkan, karena project sebelumnya
sudah terkoneksi dengan Database.
3. Buka command prompt dan ketik code :

manage.py startapp buku

4. kemudian di folder settings.py bagian INSTALLED_APPS tambahkan code :

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about',
    'buku',
]

5. di models.py di dalam app buku ketik code :

from django.db import models

class Post(models.Model):
    judul = models.CharField(max_length=255)
    sinopsis = models.TextField()

6. Buka cmd kembali dan ketik code :

manage.py makemigrations

7. masih di cmd, ketik code :

manage.py migrate

8. lakukan runserver dengan code :

manage.py runserver

9. Buka file admin.py pada app buku. Ketik kode :

from django.contrib import admin

from . models import Post

admin.site.register(post)

10. Buka kembali app buku, dan file models.py tambahkan kode :

from django.db import models

class Post(models.Model):
    judul = models.CharField(max_length=255)
    sinopsis = models.TextField()

    def __str__(self):
        return self.judul

11. Klik folder project websiteku, kemudian buka file urls.py, tambah kode :


from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', views.index),
    path('about/', include('about.urls')),
    path('about/', include('buku.urls')),

12. Klik app buku, buka file urls.py kemudian tambah kode :

from django.conf.urls import url

from . import views

urlpatterns = [
    path('buku/', views.index),

13. Buka file views.py pada app buku, kemudian tambah kode :

from django.shortcuts import render

from . models import Post

def index(request):
    postingan = Post.Object.all()

    context = {
        'TampungPostingan':postingan,
    }

    return render(request, 'buku/index.html', context)

14. Tambahkan link untuk app buku pada index.html Halaman Utama dengan code:

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
    </ul>
</body>
</html>

15. Tambahkan link untuk app buku pada index.html Halaman About

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
    </ul>
</body>
</html>



"""