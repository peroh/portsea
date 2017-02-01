import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 50},
        {"title": "How to think like a computer scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 100},
        {"title": "Learn Python in 10 minutes",
         "url": "http://www.korokithakis.net/tutorials/python",
         "views": 5}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 50},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 50},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com",
         "views": 50}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views": 50},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views": 50}
    ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}}

    for cat, cat_data in cats.iteritems():
        c = add_cat(cat)
        c.views = cat_data["views"]
        c.likes = cat_data["likes"]
        c.save()
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- %s - %s" % (c, p)

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()