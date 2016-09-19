from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Category, ProductCategories, Product, ProductImage,Brand
from .forms import UserForm, UserProfileForm
from cart import Cart

def index(request):
    category_set = Category.objects.all()
    product = Product.objects.all()
    product_images = ProductImage.objects.all()
    brands = Brand.objects.all()
    cart = Cart(request)
    j=0
    for i in cart:
        j=j+1

    # product_category_set=ProductCategories.objects.all()
    # for i in product_images:
    #     print i.product_id.id
    #     print i.product_id.name
    #     print i.image
    # for i in product:
    #     for j in product_images:
    #         if(i.id == j.product_id.id):
    #             print i.name
    # for i in product_category_set:
    #     print i.

    # print (user.id)

    context = {
               'cartitems':j,
               'categories': category_set,
               # 'product_category':product_category_set,
               'product': product,
               'product_images': product_images,
               'user': request.user,
               'brands': brands,

               }
    return render(request, 'shopify/index.html', context)


# @login_required
# def index(request):
#     return HttpResponse("Since you're logged in, you can see this text!")
# return render(request, 'loginapp/index.html')


# To create a new user
@csrf_protect
def register(request):
    # Like before, get the request's context.
    # context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # if user_form.is_valid():
            # Save the user's form data to the database.
            # request.session['username'] = username
            user = user_form.save()
            # print user_form

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            # if 'picture' in request.FILES:
            #     profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            # profile.save()

            # Update our variable to tell the template registration was successful.

            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            # print user_form.errors, profile_form.errors
            print(user_form.errors)
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

        # Render the template depending on the context. not using render_to_response
    return render(request, 'shopify/login.html'
                  , {'user_form': user_form, 'profile_form': profile_form
                      , 'registered': registered}
                  )


# Login User
@csrf_protect
def user_login(request):
    # Like before, obtain the context for the user's request.
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST' or 'GET':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # if not request.POST.get('remember_me', None):
        #     request.session.set_expiry(0)



        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # print(user)
            # Is the account active? It could have been disabled.
            if user.is_active:
                # print(user)
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                # request.session['username']=username
                login(request, user)
                return HttpResponseRedirect('/index/')
                # return render(request, 'shopify/index.html', {"username" : username})
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'register')


# def formView(request):
#    if request.session.has_key('username'):
#       username = request.session['username']
#       return render(request, 'loggedin.html', {"username" : username})
#    else:
#       return render(request, 'login.html', {})


# Use the login_required() decorator to ensure only those logged in can access the view.



# @login_required
# def categories_list(request, id=None):
#     category_set = Category.objects.all()
#     products = Product.objects.all()
#     products_images = ProductImage.objects.all()
#     products_category_set = ProductCategories.objects.all()
#     instance = get_object_or_404(Category, id=id)
#     response_data= {}
#     response_data['products']=products
#     response_data['products_images'] = products_images
#     response_data['products_category_set '] = products_category_set
#     response_data['instance'] = instance
#     return JsonResponse(response_data)




def categories_list(request, id=None):
    category_set = Category.objects.all()
    product = Product.objects.all()
    product_images = ProductImage.objects.all()
    product_category_set = ProductCategories.objects.all()
    instance = get_object_or_404(Category, id=id)
    context = {

        'categories': category_set,
        'product': product,
        'product_images': product_images,
        "instance": instance,
        "product_category_set": product_category_set,
    }
    return render(request, "shopify/categorylist.html", context)


def categories(request):
    # category_set = Category.objects.all()[:6]
    product_category_set = ProductCategories.objects.all()[:6]
    product = Product.objects.all()[:6]
    product_images = ProductImage.objects.all()[:6]
    context = {
        'product_category_set': product_category_set,
        'product': product,
        'product_images': product_images,
    }
    return render(request, "shopify/categories.html", context)


        # details
    # show categories
    # product_category_set=ProductCategories.objects.all()
    # instance=get_object_or_404(Category,id=id)
    # print instance.id
    # print "<<<<<<<<<>>>>>>>>>>>"
    # for i in product_category_set:
    #     if i.category_id.parent_id.name == instance.name:
    #         print i.product_id
    # @login_required
    # def product_list(request,id=None):
    # product_category_set=ProductCategories.objects.all()
    # instance=get_object_or_404(Category,id=id)
    # print instance.id
    # for i in product_category_set:
    #     if i.category_id.id==instance.id:
    #         print i.product_id.name
    # return HttpResponse("instance.id")


    # {%for i in product_category_set%}
    #         {%if i.category_id.parent_id.name == instance.name%}
    #             {%for img in product_images%}
    #                     {%if img.product_id.id == i.product_id.id%}
    #                     <h1>{{img.image}}</h1>
    #                     {%endif%}
    #             {%endfor%}
    #         {%endif%}
    # {%endfor%}
