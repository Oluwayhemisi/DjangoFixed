# DjangoFixed
This is a project created to Reproduce a bug in Django. 

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

