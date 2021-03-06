import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bargain_radar_project.settings')

import django
django.setup()

from radar.models import Category, Offer, User, CustomerProfile
from django.contrib.auth.models import User


def populate():
    try:
        user = User.objects.get(username__exact='john')
    except User.DoesNotExist:
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    flag = True
    customer_profile = add_customerprofile(user, flag)

    travel_cat = add_cat('Travel')

    add_offer(cat=travel_cat,
              rep=customer_profile,
              name="Antarctica",
              price=5999.00,
              top=False,
              views=326,
              likes=26,
              description='Return ticket to Antarctica. All Transport method included and travel insurance provided',
              picture='offer_images/antarctica.jpg'
    )

    add_offer(cat=travel_cat,
              rep=customer_profile,
              name="Mars",
              price=9.99,
              top=True,
              views=0,
              likes=0,
              description='One way ticket to Mars. All Transport method included and travel insurance provided',
              picture='offer_images/mars.jpg'
    )

    add_offer(cat=travel_cat,
              rep=customer_profile,
              name="Lab 715",
              price=55999.00,
              top=True,
              views=0,
              likes=0,
              description='Travel expenses paid and \ncomputer space reserved for lab 715!',
              picture='offer_images/lab715.jpg'
    )

    food_cat = add_cat("Food")

    add_offer(cat=food_cat,
              rep=customer_profile,
              name="Poison-Cola",
              price=0.01,
              top=False,
              views=0,
              likes=0,
              description='One can of Cola, cheaper than in your local shop',
              picture='offer_images/cola.jpg'
    )


    add_offer(cat=food_cat,
              rep=customer_profile,
              name="McDonald Junk",
              price=0.02,
              top=False,
              views=0,
              likes=0,
              description='Fast Food for an even cheaper price than before, \nonly on Bargain Radar',
              picture='offer_images/burger.jpg'
        )

    add_offer(cat=food_cat,
              rep=customer_profile,
              name="Water from a pipe",
              price=99.90,
              top=True,
              views=0,
              likes=0,
              description='Best quality mineral water for you! \nSpecial offer for limited time only',
              picture='offer_images/water.jpg'
    )

    sport_cat = add_cat("Sport")

    add_offer(cat=sport_cat,
              rep = customer_profile,
              name="Football",
              price=15.00,
              top=True,
              views=0,
              likes=0,
              description='One Leather size 5 football cheaper than all sport stores',
              picture='offer_images/football.jpg'
    )

    add_offer(cat=sport_cat,
              rep=customer_profile,
              name="Wilson Junior Tennis Racket",
              price=32.00,
              top=False,
              views=0,
              likes=0,
              description='Small child sized tennis racket',
              picture='offer_images/racket.jpg'
    )

    add_offer(cat=sport_cat,
              rep=customer_profile,
              name="Puma Gym Trainers",
              price=42.00,
              top=False,
              views=0,
              likes=0,
              description='High quality all weather condtion trainers, many sizes available',
              picture='offer_images/trainers.jpg'
    )

    dvd_cat = add_cat("DVDs")

    add_offer(cat=dvd_cat,
              rep=customer_profile,
              name="Dumb and Dumber",
              price=7.99,
              top=True,
              views=0,
              likes=0,
              description='Finest classic comedy on DVD cheaper than ever',
              picture='offer_images/dumbdumber.jpg'
    )

    add_offer(cat=dvd_cat,
              rep=customer_profile,
              name="Bourne Identity",
              price=5.99,
              top=False,
              views=0,
              likes=0,
              description='First DVD of the bourne series available now!',
              picture='offer_images/bourne.jpg'
    )

    add_offer(cat=dvd_cat,
              rep = customer_profile,
              name="The Hobbit: Desolation of Smaug",
              price=6.99,
              top=False,
              views=0,
              likes=0,
              description='Hobbit DVD available for a limited time only',
              picture='offer_images/hobbit.jpg'
    )
    user.save()

    for c in Category.objects.all():
        for o in Offer.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(o))


def add_offer(cat, rep, name, price, top, picture, amount=0, views=0, likes=0, description=""):
    o = Offer.objects.get_or_create(category=cat,representative=rep, name=name, price=price)[0]
    o.top = top
    o.picture = picture
    o.amount = amount
    o.views = views
    o.likes = likes
    o.description = description
    o.save()
    return o


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


def add_customerprofile(user,client):
    c = CustomerProfile.objects.get_or_create(user = user,representative = client)[0]
    return c


if __name__ == '__main__':
    print "Starting BargainRadar population script..."
    populate()