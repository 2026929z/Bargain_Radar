from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import Offer, Category, CustomerProfile
from forms import CustomerForm, CustomerProfileForm

def index(request):
    feature_offer1 = Offer.objects.get(name='McDonald Junk')
    feature_offer2 = Offer.objects.get(name='Lab 715')
    feature_offer3 = Offer.objects.get(name='Water from a pipe')

    top_offers = Offer.objects.filter(top = True)
    categories_list = Category.objects.all()
    offers_list = Offer.objects.all()

    context_dict = {'offer1': feature_offer1,
                    'offer2': feature_offer2,
                    'offer3': feature_offer3,
                    'categories':categories_list,
                    'offers':offers_list,
                    'top_offers':top_offers}
    
    return render(request,'radar/index.html', context_dict)

def category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    category_title = category.title
    offer = Offer.objects.filter(category=category)
    context_dict = {'category_title':category_title, 'offer': offer}

    return render(request,'radar/category.html', context_dict)

def offer(request,offer_id):
    offer = Offer.objects.get(id = offer_id)
    context_dict = {'offer':offer}
    return render(request,'radar/offer.html', context_dict)

def showLogin(request):
    return render (request, 'radar/login.html')

def contact(request):
    return render(request, 'radar/contact-us.html')

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
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

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
                return HttpResponse("Account does not exists")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'radar/index.html', {})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/bargain_radar/')

# @login_required
def basket(request):
    # customer = Customer.objects.get(username=request.Customer.username)
    # basket = Customer.Basket
    # item = basket.item
    # context_dict = {'item':item,'customer':customer,'basket': basket}

    return render(request,'radar/cart.html') #,context_dict)

def checkout(request):
    return render(request, 'radar/checkout.html')

def shop(request):
    return render(request, 'radar/shop.html')

def details(request):
    return render(request, 'radar/product-details.html')

def blog(request):
    return render(request, 'radar/blog.html')

def single_blog(request):
    return render(request, 'radar/blog-single.html')

def error(request):
    return render(request, 'radar/404.html')

##def remove_offer_basket(request):


##def our_clients(request):
#
# @login_required
# def like_offer(request):
#
#     offer_id = None
#     if request.method == 'GET':
#         offer_id = request.GET['offer_id']
#
#     likes = 0
#     if offer_id:
#         offer = Offer.objects.get(id=int(offer_id))
#         if offer:
#             likes = offer.likes + 1
#             offer.likes =  likes
#             offer.save()
#
#     return HttpResponse(likes) ##Uses AJAX



# @login_required
# def write_review(request,category_name_slug,offer_name_slug):
# 	if request.method == 'POST':
# 		text = request.POST['text']
#     offer = Offer.objects.get(slug=offer_name_slug)
#     offer.review = text
#
#     return HttpResponse(review) ##Uses AJAX

# @login_required
# def add_offer(request):
# 	if request.method == 'POST':
#         form = offerForm(request.POST)
#     ##there should be code here specifying the category for the deal. A menu to choose from
#     if form.is_valid():
#             if cat:
#                 offer = form.save(commit=False)
#                 offer.category = cat
#                 offer.views = 0
#                 offer.likes = 0
#                 offer.save()
#
#         else:
#             print form.errors
#     else:
#         form = offerForm()
#     context_dict = {'form':form, 'category': cat}
#
#     return render(request, 'rango/profile.html', context_dict)

# @login_required
# def search(request):
#
#
#     result_list = []
#
#     if request.method == 'POST':
#         query = request.POST['query'].strip()
#
#         if query:
#             result_list = run_query(query)
#
#     return render(request, 'rango/search.html', {'result_list': result_list})


# def about(request):
#     context_dict = {'Message':'Bargain Radar is bla bla bla'}
#     response = render(request,'bargain_radar/about.html',context_dict)
 