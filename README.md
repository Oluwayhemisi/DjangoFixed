# DjangoFixed
This is a project created to Reproduce a bug in Django. 
#30386 (Admin foreign key widgets don't quote keys.)

# To get started
$ git clone git@github.com/USERNAME/{{ project_name }}.git

$ cd {{ project_name }}

Install project dependencies:

$ pip install -r requirements/local.txt

Then simply apply the migrations:

$ python manage.py migrate

# To run Project

You can now run the development server:

$ python manage.py runserver
 
$ Go to the /admin/ URL of your Django application, find the Room object you created, and click on the "Change" link   next to it. On the change page, click on the link or change icon for the House foreign key to see the message         "House with ID "@" doesn't exiat. Perharps it was deleted


# Results




![PK!.png](https://github.com/Oluwayhemisi/DjangoFixed/blob/main/PK1.jpeg)
![](../../Pictures/PK2.jpeg)
![](../../Pictures/PK3.jpeg)
