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



# Data Sources
* https://www.ibdb.com/
* https://en.wikipedia.org/wiki/List_of_musicals:_A_to_L
* https://en.wikipedia.org/wiki/List_of_musicals:_M_to_Z

The wiki pages have a list of the productions:  
* https://en.wikipedia.org/wiki/42nd_Street_(musical)

# Notes
## 2023-12-03
* Finding the birth and death dates of the people is kinda difficult
* Adding the people in and the roles is very tedious and should be automated as much as possible

## 2023-12-04

* Performance dates should not be hard-coded  
some objects need to be tied to a specific performance, i.e. casting and reviews. However, casting can span many 
performances. So rather than create a record for every casting/performance date, the casting should include a time span.
This time span should be restricted to the time span of the relative production. Then to look up a casting/performance, there must be a function to get the overlapping time spans. 
* A similar case for reviews: review dates should be restricted to within the time span of the relevant production. And then a validation function ensures there is a performance on that date, if that information is available. 
* Remember that there are multiple performances on some days, so there can't be a unique date constraint for a certain performance.
* The performance object will have to include a showtime member.


