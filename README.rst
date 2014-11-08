====
G43 Exercise
====

G43 Exercise is a simple Django website that contains only two pages:
	A list page that enumerates all articles contained on the site
	A detail page that displays the contents of a particular article
	
	Note: Functionality for displaying random articles does not include expressions to prevent
	articles dated in the future from being displayed even though they are "not yet published".
	Time constraints have prevented this from being implemented in the initial release 0.1.
	
	Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "g43exercise" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = (
        ...
        'g43exercise',
    )

2. Make sure that your MEDIA_URL points to '/g43exercise/media/' 	
	
3. Include the polls URLconf in your project urls.py like this::

    url(r'^g43exercise/', include('g43exercise.urls', namespace="g43")),

4. Run `python manage.py migrate` to create the polls models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an article (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/g43exercise/ to view the website.