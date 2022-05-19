"""
1. Jalankan terlebih dahulu projek di CMD
2. Buka VSC dan buka folder django projek yang dibuat
3. isi dengan code :

from django.contrib import admin
from django.urls import path
from perpustakaan.views import buku

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', index),
]

(views menjadi namespace)

4. Buat folde file py dengan nama views dengan isi code :

from django.shortcuts import render

def buku(request):
    return render(request, 'index.html')

5. Buat folder dengan nama templates
6. Kemudian di file settings.py isi berisi code :

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

untuk DIRS akan mencari folder dengan nama TEMPLATES
untuk APPS_DIRS mencari folder dengan nama TEMPLATES di semua app

7. Di folder templates buat file index.html dengan codenya :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOME</title>

</head>
<body>
    
    <h2>Halaman Utama</h2>
    <ul>

        <li><a href="/">Home</a></li>
    </ul>
</body>
</html>

8. Untuk membuat App menggunakan CMD dengan code :

manage.py startapp about

9. Di file urls tambahkan code :

from django.contrib import admin
from django.urls import path
from perpustakaan.views import buku

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', views.index),
    path('about/', include('about.urls')),

10. di App About Buat file urls.py dengan code :

from django.urls import url

from . import views

urlpatterns = [
    path('buku/', views.index),

11. Di folder setting bagian variabel INSTALLED_APPS tambahkan code :

'about',

dibarisbaru

12. kemudian buat folder templates di folder about
13. Setelah itu buat lagi folder about didalam folder templates
14. di file about buat file index.html dengan code :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOME</title>

</head>
<body>
    
    <h2>Halaman Utama</h2>
    <ul>

        <li><a href="/">Home</a></li>
        <li><a href="about/">About</a></li>
    </ul>
</body>
</html>

15. Kemudian di file views.py tambahkan code seperti diatas :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOME</title>

</head>
<body>
    
    <h2>Halaman Utama</h2>
    <ul>

        <li><a href="/">Home</a></li>
        <li><a href="about/">About</a></li>
    </ul>
</body>
</html>

16. Kemudian jalankan addresnya dengan menambahkan slash(/)about
"""