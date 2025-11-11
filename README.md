# Assignment 3: Django Frameworks and Energy Quality Attribute
Team Members and Contributions
**Group 8 – CRN 45740** 
| Member | Contributions Phase 1 |
|--------|--------------------------------|
| Geraline Chavez 100890130 | Question 2 Part A & B (Tactics 1, 2) |
| Christopher Lui 100912564 | Question 1 Part B |
| Nicholas Furtado 100908880 | Question 1 Part A & Question 2 Part B (Tactics 3, 4) |

Every team members participated proportionally in review, editing, and integration of the first phase of the project. 

---

## Overview

This project is divided into two parts:

1. **Question 1 – Django ORM Implementation:**  
   Using Django’s Object-Relational Mapper (ORM) in standalone mode to simulate the functionality of a cash register.  
   The focus for this part is database population and data handling.

2. **(Attached as PDF to repository but submitted separately on canvas) Question 2 – Energy Efficiency Quality Attribute:**  
   Creating a **Concrete Energy Efficiency Scenario** for the *CalmMind* anxiety-tracking application, followed by identification of multiple architectural or design tactics to improve the system’s energy efficiency.

---

### **Files**
## Project Structure
--------------------------------
```
SOFTWARELAB3/
│
├─ lab3django/ # Django project configuration folder
│ ├─ pycache/
│ ├─ init.py
│ ├─ asgi.py
│ ├─ settings.py
│ ├─ urls.py
│ └─ wsgi.py
│
├─ mainapp/ # Django app folder
│ ├─ pycache/
│ ├─ migrations/
│ ├─ init.py
│ ├─ admin.py
│ ├─ apps.py
│ ├─ models.py
│ ├─ tests.py
│ ├─ urls.py
│ └─ views.py
│
├─ venv/ # Python virtual environment
│ ├─ Include/
│ ├─ Lib/
│ └─ Scripts/
│
├─ .gitignore
├─ pyvenv.cfg
├─ db.sqlite3 # SQLite database file
├─ main.py
└─ manage.py # Django management script
```
---
**Quick Setup & Run Instructions (Windows)**

Create a folder for your project on your local machine
```
mkdir myproject; cd myproject
```
Create a virtual environment and install django
```
python -m venv venv; source venv/bin/activate; pip install django
```
Clone the repository from GitHub:
```
git clone git@github.com:dancaron/Django-ORM.git; cd Django-ORM](https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-8-crn-45740.git
```
Initialize the database
```
python manage.py makemigrations db; python manage.py migrate
```
Run the project
```
python main.py
```
## Part 1 – Django ORM Implementation (Cash Register App)

### **Objective**
To use the Django ORM framework to populate a local SQLite database with product information (UPC, name, and price), simulating a cash register’s product catalog.

Create a virtual environment and install Django  
<img width="1077" height="620" alt="Screenshot 2025-11-09 214258" src="https://github.com/user-attachments/assets/45a5a291-8e25-4ee7-8b51-4898b2be3326" />

Initialize the database and run the project 
<img width="1070" height="580" alt="Screenshot 2025-11-09 214341" src="https://github.com/user-attachments/assets/47fabb4e-bd48-4ab6-b096-de7fd4456d0c" />

<img width="1169" height="330" alt="image" src="https://github.com/user-attachments/assets/26c18fca-f813-40d2-88cf-3d4091f856a8" />

<img width="1170" height="535" alt="image" src="https://github.com/user-attachments/assets/506e9373-e51d-469d-b16c-655c465b5518" />

Besides main.py, we also added changes for model.py and apps.py, allowing the GUI to work properly with the UPC codes, and display them accordingly.



## Part 2 - Energy Efficency Quality Attribute
*Attached as PDF to repository but submitted separately on canvas
- *Concrete Energy Efficiency Scenario* of *CalmMind* anxiety-tracking application
- *Architectural and design tactics* to improve the system’s energy efficiency 

--------------------------------------------------------------------------------------------------
---
README provided with the assignment 

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-cPJVYMd)
Django ORM Standalone
=====================

![Django](https://img.shields.io/badge/Django_ORM-Standalone-blue)
![Python](https://img.shields.io/badge/Python-yellow)

Use the database components of Django without having to use the rest of Django (i.e. running a web server)! :tada: A typical use case for using this template would be if you are writing a python script and you would like the database functionality provided by Django, but have no need for the request/response functionalty of a client/server web application that Django also provides. 

With this project template you can write regular python scripts and use Django's excellent ORM functionality with the database backend of your choice. This makes it convienient for Djangonauts to write database driven python applications with the familiar and well polished Django ORM. Enjoy.

:gear: Requirements
-------------------
- Last tested successfully with Python 3.10.4 and Django 5.0.6
- Create venv and pip install django to import the required modules.

:open_file_folder: File Structure
---------------------------------
```
django-orm/
├── db/
│   ├── __init__.py
│   └── models.py
├── main.py
├── manage.py
├── README.md
└── settings.py
```

__The main.py file is the entry point for the project, and where you start your code. You automatically get access to your models via ```from db.models import *```
Think of it like a plain old python file, but now with the addition of Django's feature-rich models.__ :smiling_face_with_three_hearts:

__The db/models.py is where you configure your typical Django models.__ There is a toy user model included as a simple example. After running the migrations command in the quick setup below, a db.sqlite3 file will be generated. The settings.py file is where can swap out the sqlite3 database for another database connection, such as Postgres or AmazonRDS, if you wish. For most applications, sqlite3 will be powerful enough. But if you need to swap databases down the road, you can easily do so, which is one of the benefits of using the Django ORM. 

:rocket: Quick Setup
--------------------
Create a folder for your project on your local machine
```
mkdir myproject; cd myproject
```
Create a virtual environment and install django
```
python -m venv venv; source venv/bin/activate; pip install django
```
Download this project template from GitHub
```
git clone git@github.com:dancaron/Django-ORM.git; cd Django-ORM
```
Initialize the database
```
python manage.py makemigrations db; python manage.py migrate
```
Run the project
```
python main.py
```

Feel free to send pull requests if you want to improve this project.

:crystal_ball: Example
----------------------
After running Quick Start above: 

Code in db/models.py:
```
# Sample User model
class User(models.Model):
    name = models.CharField(max_length=50, default='Dan')

    def __str__(self):
        return self.name
```
Code in main.py:
```
# Seed a few users in the database
User.objects.create(name='Dan')
User.objects.create(name='Robert')

for u in User.objects.all():
    print(f'ID: {u.id} \tUsername: {u.name}')
```
Output from command: ```python main.py```
```
ID: 1	Username: Dan
ID: 2	Username: Robert
```

:mortar_board: Django Models
----------------------------

Link: [How to Use Django Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)

License
-------

The MIT License (MIT) Copyright (c) 2024 Dan Caron

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
