"""
1.  Relasi Dua Model pada App
2. Buka file models.py pada app buku, tambahkan kode :

from django.db import models

class Kategori(models.Model):
    kategori = models.CharField(max_length=100)
    
    def __str__(self):
        return self.kategori

class Post(models.Model):
    judul = models.CharField(max_length=255)
    sinopsis = models.TextField()
    
    def __str__(self):
        return self.judul

3. Buka cmd, ketik code :

manage.py makemigrations

4. kemudian Ketik code :

manage.py migrate

5. Buka file admin.py pada app buku, tambahkan kode :

from django.contrib import admin

from . models import Post, Kategori

admin.site.register(Post)
admin.site.register(Kategori)

6. Buka kembali file models.py pada app buku. Tambahkan kode :


from django.db import models

class Kategori(models.Model):
    kategori = models.CharField(max_length=100)
    
    def __str__(self):
        return self.kategori

class Post(models.Model):
    judul = models.CharField(max_length=255)
    sinopsis = models.TextField()
    ketegori = models.ForeignKet(Kategori, on_delete =models.SET_NULL, null=True)
    
    def __str__(self):
        return self.judul

7. lakukan migrasi
8. eksekusi migrasi

"""