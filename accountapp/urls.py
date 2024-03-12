from django.urls import path
from accountapp import views
urlpatterns=[
     path('signup/',views.signup,name='signup'),
     path('login/',views.loginUser,name='login'),
     path('logout/',views.logoutUser,name='logout'),
     path('dashboard/',views.dashboard,name='dashboard'),
]