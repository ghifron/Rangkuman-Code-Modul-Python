"""

1. Buat folder dengan nama static
2. kemudian di file settings bagian STATIC_URL tambahkan code :

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

3. Buat folder dengan nama img di folder static
4. copy gambar yang akan dimasukan
5. Buat folder static, about, dan img di dalam app about.
6. copy lagi gambar yang akan dimasukan
7. jalankan server
8. di file index.html di folder template dengan code :

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOME</title>

</head>
<body>
    
    <img src="{% static 'img/home.jpg %}" alt="">
    <h2>Halaman Utama</h2>
    <ul>

        <li><a href="/">Home</a></li>
        <li><a href="about/">About</a></li>
    </ul>
</body>
</html>

9. begitu juga dengan about dengan code :

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOME</title>

</head>
<body>
    
    <img src="{% static 'about/img/about.jpg %}" alt="">
    <h2>Halaman Utama</h2>
    <ul>

        <li><a href="/">Home</a></li>
        <li><a href="about/">About</a></li>
    </ul>
</body>
</html>

10. Buat folder css didalam folder static utama
11. buat file style.css
13. sesuaikan dengan index.html utama dengan code :

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
    </ul>
</body>
</html>

14. begitu juga dengan about dengan code :


"""