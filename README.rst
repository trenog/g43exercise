====
G43 Exercise
====

	G43 Exercise is a simple Django website that contains only two pages:
	A list page that enumerates all articles contained on the site
	A detail page that displays the contents of a particular article
	
	Note: After initial release 0.1 the exercise has been updated with new style coding,
	test cases, and updates to prevent future dated articles from ever displaying in the
	context of the Index or Detail pages. The website will error to a 404 page if only future
	dated articles are found in the host database.
	
	Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "g43exercise" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = (
        ...
        'g43exercise',
    )

2. Make sure that your MEDIA_URL points to '/g43exercise/media/' 	

3. Add functionality to your settings.py file to support TEMPLATEs and STATIC files
	
4. Include the polls URLconf in your project urls.py like this::

    url(r'^g43exercise/', include('g43exercise.urls', namespace="g43")),

5. Run `python manage.py migrate` to create the Article model.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an article (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/g43exercise/ to view the website.