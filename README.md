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


## 2023-12-08
* There are touring productions for which there is no constant venue

** Cast/Crew Dates **
There is somewhat a problem for associating cast and crew with productions. I thought using a timespan would be easier 
than individual dates. It is easier to enter that information because you don't need to make an individual record of 
each performance. However, in the cases where an agent (cast/crew) are associated with a production for many disjointed 
performances, this can be effectively the same model as associating them with individual performances. Additionally, 
a cast/crew might be associated with a performance which is in the middle of a span of performances associated with 
another agent. We could split the latter agents' associations into two or more spans, which in the worst case would be a
checkerboard of one agent alternating with the other.

I think that including the time span of association is better than individual performances. Although it would be more 
accurate to associate agents with individual performances (which are themselves associated with time/date), it is more 
economical to use time spans. Furthermore, the historical records for these associations are incomplete on average, 
and I imagine commonly nonexistent. So timespans will work for now.

If at a later date there is a need for cast/crew to be associated with individual performances, maybe there can be a 
more sparse cast/crew table tied to a performance. This would be useful to highlight some notable special guest star or 
an understudy performing.

Reviews however, should continue to be associated with individual performances, which, again, need to be associated with
a date and time.

## 2023-12-30
There should be a separate character table.  
Cast members should still be included in the cast/crew table; however, there should be an optional field that is the 
character if the role is "cast member".

There could be "understudy" and "swing" roles that are similar to "cast member". This would create a distinction between
 these types of performing roles. Although I think it is easier to add some boolean fields to this effect.  
I will add "swing" & "understudy" boolean fields to the `CastCrew` model.

**Cast Crew Dates**
I think it makes sense to leave the start and end dates of the performances blank. Upon display I can use the related 
production start and end dates. This allows more specific dates to be recorded for performers/crew, but is not required 
if that information is not available.

**Ratings Beyond The Performance**  
This platform is primarily for rating the performance level, e.g. the last performance of the original broadway 
production of "Cats". However, we could allow the user to rate the actor's acting performance and singing performance.
The ratings could be semi-hierarchical: Show, Production, Performance (entire cast), Song, Actor.


## 2023-12-31
The data pipeline will be quite important. We really need easy (not necessarily fast) import into the system. 
Out data pipeline needs are:
* Accurate
* Easy
* Timely - When shows start, the necessary information must be available

You can import the div-based table from the broadway database. However, it still requires some post-processing. 
It's not too bad. However, any amount of manual data processing is kind of a problem. Ultimately you could rely on the 
users to provide and process the data. But then the input forms need to be quite good.

## 2024-02-17
I don't know if you need to make this a scheduled set of tasks.  
This is really just a one time import whenever there is a show. There is no real reason to import historical shows - no 
one can review them.  
What **would** be helpful is an automatic way to upload the information from a photo/pdf/csv.  

Also removing anything historical musicals would also remove the need to put in death dates of the people.


