from django.conf.urls import url
from . import views
from . import new_views

app_name = 'shopify'
urlpatterns = [
    #ex--> localhost:8000/
    url(r'^$', views.register, name='index'),
    #ex--> localhost:8000/register
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    #ex--> localhost:8000/login
    url(r'^login/$', views.user_login, name='login'),
    #ex--> localhost:8000/logout
    url(r'^logout/$', new_views.user_logout, name='logout'),
    # ex--> localhost:8000/index
    url(r'^index/$', views.index, name='index'),
    # ex--> localhost:8000/list
    url(r'^list/(?P<id>[0-9]+)$', views.categories_list, name='list'),
    # ex--> localhost:8000/productlist
    # url(r'^productlist/(?P<id>[0-9]+)/$', views.product_list, name='products'),
    url(r'^index/$', views.index, name='index'),
    # ex--> localhost:8000/categories/
    url(r'^categories/$', views.categories, name='categories'),
    # ex--> localhost:8000/subcategories/
    url(r'^subcategories/(?P<id>[0-9]+)/$', new_views.subcategories_list, name='subcategories'),
    # ex--> localhost:8000/products/
    url(r'^products/$', new_views.products, name='products'),
    # ex--> localhost:8000/brands/1
    url(r'^brands/(?P<id>[0-9]+)/$', new_views.brands, name='brands'),
    #ex--> localhost:8000/media
    url(r'^media/$', new_views.cart_detail, name='cart_detail'),
    # ex--> localhost:8000/add
    url(r'^add/(?P<id>\d+)/$', new_views.cart_add, name='cart_add'),
    # ex--> localhost:8000/remove
    url(r'^remove/(?P<product_id>\d+)/$', new_views.cart_remove, name='cart_remove'),

]