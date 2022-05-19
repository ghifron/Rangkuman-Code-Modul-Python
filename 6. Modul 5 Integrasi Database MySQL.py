"""

1. Menginstal modul client
2. Buka command prompt
3. masuk terlebih dahulu ke Virtual Environment
4. kemudian ketik code :

pip install mysqlclient

5. Buka xampp Anda, aktifkan Apache dan MySQL
6. Buka project Anda di Visual Studio Code, buka file settings.py di dalam folder
project websiteku. Kemudian tambahkan kode :

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangowebsiteku',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306', 
    }
}

7. Buka phpmyadmin pada browser. Buatlah database dengan nama
djangowebsiteku
8. Buka kembali cmd, ketik manage.py migrate

Migration adalah sebuah fasilitas yang digunakan untuk mempermudah kita ketika ada
perubahan dalam database. Pada langkah ini kita membuat tabel, field, dan record
untuk aplikasi yang sudah didefinisikan di dalam list INSTALLED_APPS pada
settings.py ke database djangowebsiteku.

"""
