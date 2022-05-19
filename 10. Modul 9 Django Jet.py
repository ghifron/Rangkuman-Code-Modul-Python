"""

1. Pertama install terlebih dahulu modul django net di command prompt dengan code :

pip install django-jet

2. Pada VSCode, Open Folder kemudian buka file settings.py pada project
directory. atur kode :

INSTALLED_APPS = [
    'jet',
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

3. Buka file urls.py utama. Tambahkan kode :

from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('/', views.index),
    path('about/', include('about.urls')),
    path('buku/', include('buku.urls')),
    path('tamu/', include('tamu.urls')),
]


4. Kembali buka cmd, ketik code L

manage.py migrate jet

5. Buka file settings.py pada project directory. Sesuaikan kode :

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
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

6. Buka file urls.py utama. Tambahkan kode :

from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('/', views.index),
    path('about/', include('about.urls')),
    path('buku/', include('buku.urls')),
    path('tamu/', include('tamu.urls')),
]

7. Kembali buka cmd, ketik :

manage.py migrate dashboard

8. lakukan runserver
9. lakukan login http://127.0.0.1:8000/admin/

"""