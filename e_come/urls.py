"""
URL configuration for e_come project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from  django.conf.urls.static import static
from .import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base,name='base'),
    path('', views.index,name='index'),
    path('singup', views.singup ,name="signup"),
    path('accounts/',include ('django.contrib.auth.urls') ),

#contact
    path('contact_us', views.contact_us ,name="contact"),
#addtoacrd
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
#chakeout
    path('chakeout/', views.chakeout ,name="chakeout"),   
#productdetails
    path('product_details/',views.product_details,name='product_details'),
#productdetails_page
    path('product_details/<str:id>',views.product_details_page,name='product_details_page') ,  
#search
   path('search/',views.search,name='search')     

]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT )















