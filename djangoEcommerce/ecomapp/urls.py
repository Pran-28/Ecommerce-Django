

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.loginRender, name='loginRenderer'),
    path("login/", views.login ,name="login"),
    path("logout/", views.logout, name='logout'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    
]
