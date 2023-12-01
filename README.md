# Django Notes

* You create the website manager first. Then you make apps within the website manager.

## Add Models 
* Create models and register them with the admin/manager

Once you add the model you need the database to reflect this new table
```bash
python manage.py makemigrations;
python manage.py migrate;
```


# Displaying Data
* You should use generic views when possible
* Use dynamically generated urls within the templates - although this might be different with unicorn


# Tests
You put a pytest-like python script within each app directory

You can run tests:
```bash
python manage.py test polls
```

# Admin Page
You can customize the admin page if you want.  
Customize the admin page to show info from related models.  
You can also customize the display format and filtering/sorting options for a given model.  

# Unicorn
