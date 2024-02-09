# Portfolio

Portfolio App using Django Backend with authentication system.

### GETTING STARTED

1 - Install requirements 
```
pip install -r requirements.txt
```

2 - Install postgresql and pgadmin and create a database inside pgadmin. Then change 
the database settings inside Settings.py or simply use default sqlite3 database.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Your database name',
        'USER': 'postgres',
        'PASSWORD': 'Your postgres password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

3 - Make Migrations 
```
python manage.py makemigrations
python manage.py migrate
```

4 - Runserver on port 8000
```
python manage.py runserver

http://127.0.0.1:8000/
```

5 - Create superuser 
```
python manage.py createsuperuser
```

### Changes for Contact Page
- In settings.py, you have to give your email id and password. I did this using 
environment variable. If you know how to use environment variable, you can do the 
same, or you can simply give your account credentials directly in settings.py file.
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
```

- Login to gmail through host email id in your browser and open following link and turn it ON
```
https://myaccount.google.com/lesssecureapps
```

<hr>

### ScreenShots
<hr>

### Homepage
![HomePage](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/HomePage.png?raw=true)

### About
![AboutPage](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/About.PNG?raw=true)
![AboutPage](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/About2.PNG?raw=true)

### Contact
![ContactPage](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/Contact.PNG?raw=true)

### Registration
![Registration](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/Registration.PNG?raw=true)

### Login
![Login](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/Login.PNG?raw=true)

### Profile
![Profile](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/Profile.PNG?raw=true)

### Change Password
![ChangePassword](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/ChangePassword.PNG?raw=true)

### Add/Update Project (Same for Blog Post)
![AddProject](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/AddProjectPost.PNG?raw=true)

### Projects
![Projects](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/Project.PNG?raw=true)

### Project Detail View
![ProjectDetail](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/ProjectDetail.PNG?raw=true)

### Blog
![Blog](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/Blog.PNG?raw=true)

### Blog Post
![BlogPost](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/BlogPost.PNG?raw=true)

### Messages
![Messages](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/Inbox.PNG?raw=true)

### Message Detail View
![MessageDetails](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/InboxDetail.PNG?raw=true)

### Reply Message
![Reply](https://github.com/ShihabAhmed09/Portfolio/blob/main/static/screenshots/Reply.PNG?raw=true)
