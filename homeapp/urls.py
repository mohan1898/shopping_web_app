from django.urls import path
from homeapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('thanks/',views.thanks,name='thanks'),
    path('shop/',views.shop,name='shop'),
    path('men/',views.men,name='men'),
    path('category/<int:id>',views.category,name='category'),
    path('women/',views.women,name='women'),
    path('cart/<int:id>',views.cart,name='cart'),
]
