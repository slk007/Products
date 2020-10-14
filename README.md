### Products and Reviews

* Prequisites
    * python3

**Make a copy of this repo in your local PC**
<br>
**Go inside the 'Product' Folder and open a cmd/termimal**
<br>
**Then follow below Steps:**

Install all the required libraries for the project:
```
pip install -r requirements.txt
```

Create a superuser:
```
python manage.py createsuperuser
```

Make Migrations:
```
python manage.py makemigrations
```

Run Migrations
```
python manage.py migrate
```

Run Server:
```
python manage.py runserver
```
And Go to http://127.0.0.1:8000/ on Browser

<br>

**Products can only be added from the admin panel:**
http://127.0.0.1:8000/admin/