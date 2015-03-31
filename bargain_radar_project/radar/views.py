from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from models import Offer, Category, CustomerProfile, Basket
from forms import CustomerForm, CustomerProfileForm, OfferForm


def index(request):
    context_dict = {}

    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.username)
        try:
            customer = CustomerProfile.objects.get(user=user)
            context_dict['customer'] = customer
        except CustomerProfile.DoesNotExist:
            logout(request)

    feature_offer1 = Offer.objects.get(name='McDonald Junk')
    feature_offer2 = Offer.objects.get(name='Lab 715')
    feature_offer3 = Offer.objects.get(name='Water from a pipe')

    top_offers = Offer.objects.filter(top=True)
    categories_list = Category.objects.all()
    offers_list = Offer.objects.all()

    context_dict['offer1'] = feature_offer1
    context_dict['offer2'] = feature_offer2
    context_dict['offer3'] = feature_offer3
    context_dict['categories'] = categories_list
    context_dict['offers'] = offers_list
    context_dict['top_offers'] = top_offers
    
    return render(request, 'radar/index.html', context_dict)


def category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    category_title = category.title
    offer = Offer.objects.filter(category=category)
    context_dict = {'category_title': category_title, 'offer': offer}

    return render(request, 'radar/category.html', context_dict)


def offer(request, offer_id):
    categories_list = Category.objects.all()
    offers_list = Offer.objects.all()
    offer = Offer.objects.get(id=offer_id)
    context_dict = {'offer': offer, 'categories': categories_list, 'offers': offers_list}
    return render(request, 'radar/product-details.html', context_dict)


def showLogin(request):
    return render(request, 'radar/login.html')


def contact(request):
    user = User.objects.get(username=request.user.username)
    customer = CustomerProfile.objects.get(user=user)

    return render(request, 'radar/contact-us.html', {'customer': customer})


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = CustomerForm(data=request.POST)
        profile_form = CustomerProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = CustomerForm()
        profile_form = CustomerProfileForm()

    return render(request,
                  'radar/login.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/bargain_radar/')
            else:
                return render(request, 'radar/login.html', {'message': "Account does not exists"})
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'radar/login.html', {'message': "Invalid login details supplied."})
    else:
        return render(request, 'radar/index.html', {})


@login_required
def user_logout(request):
    offers = Offer.objects.all()
    for curr_offer in offers:
        curr_offer.amount = 0
        curr_offer.save()

    user = User.objects.get(username=request.user.username)
    customer = CustomerProfile.objects.get(user=user)
    try:
        basket = Basket.objects.get(customer=customer)
        basket.delete()
    except Basket.DoesNotExist:
        pass

    logout(request)

    return HttpResponseRedirect('/bargain_radar/')


@login_required
def add_basket(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    user = User.objects.get(username=request.user.username)
    customer = CustomerProfile.objects.get(user=user)

    try:
        basket = Basket.objects.get(customer=customer)
    except Basket.DoesNotExist:
        basket = Basket(customer=customer, total=0)
        basket.save()

    offer.amount += 1
    offer.save()

    basket.item.add(offer)
    basket.total = float(basket.total) + float(offer.price)
    basket.save()
    items = basket.item.all()
    context_dict = {'items': items, 'basket': basket}

    return redirect('/bargain_radar/basket/', context_dict)


@login_required
def remove_basket(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    offer.amount -= 1
    offer.save()

    user = User.objects.get(username=request.user.username)
    customer = CustomerProfile.objects.get(user=user)
    basket = Basket.objects.get(customer=customer)
    basket.total = float(basket.total) - float(offer.price)

    if offer.amount == 0:
        basket.item.remove(offer)

    basket.save()
    items = basket.item.all()
    context_dict = {'items': items, 'basket': basket}

    return redirect('/bargain_radar/basket/', context_dict)


@login_required
def remove_offer(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    user = User.objects.get(username=request.user.username)
    offer.delete()
    items = Offer.objects.filter(representative=user)
    context_dict = {'items': items}

    return redirect('/bargain_radar/client_offers/', context_dict)


@login_required
def basket(request):
    user = User.objects.get(username=request.user.username)
    customer = CustomerProfile.objects.get(user=user)
    try:
        basket = Basket.objects.get(customer=customer)
        items = basket.item.all()
    except Basket.DoesNotExist:
        basket = None
        items = None

    context_dict = {'items': items, 'customer': customer, 'basket': basket}

    return render(request, 'radar/cart.html', context_dict)


@login_required
def client_offers(request):
    user = User.objects.get(username=request.user.username)
    customer = CustomerProfile.objects.get(user=user)
    items = Offer.objects.filter(representative=customer)
    context_dict = {'items': items, 'customer': customer}

    return render(request, 'radar/client_offers.html', context_dict)


@login_required
def checkout(request):
    return render(request, 'radar/checkout.html')


@login_required
def add_offer(request):
    user = User.objects.get(username=request.user.username)
    representative = CustomerProfile.objects.get(user=user)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
                offer = form.save(commit=False)

                try:
                    offer.picture = request.FILES['picture']
                except:
                    offer.picture = 'default_offer_img.jpg'

                offer.top = False
                offer.views = 0
                offer.likes = 0
                offer.representative = representative
                offer.save()   
                return HttpResponseRedirect('/bargain_radar/')    
        else:
            print form.errors
    else:
        form = OfferForm()

    context_dict = {'categories': categories, 'form': form, 'customer': representative}

    return render(request, 'radar/add_offer.html', context_dict)


def shop(request):
    return render(request, 'radar/shop.html')


def details(request):
    return render(request, 'radar/product-details.html')


def error(request):
    return render(request, 'radar/404.html')


def account(request):
    return render(request, 'radar/account.html')