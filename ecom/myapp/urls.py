from django.urls import path
from . import views

urlpatterns = [
    path('', views.getindex, name='index'),
    path('category/<name>', views.getcategory, name='category'),
    path('register/', views.Getregister, name='register'),
    path('login/', views.GetLogin, name='login'),
    path('logout/', views.Getlogout, name='logout'),
    path('product_details/<int:id>', views.Getproduct_details, name='product_details'),
    path('pay/<int:id>', views.Getpays, name='pay'),
    path('brand/<name>', views.Getbrand, name='brand'),
    path('comment/<int:id>', views.Getcomment, name='comment'),
    path('cart/<int:id>/<name>', views.Getcart, name='cart'),
    path('gocart/<int:id>', views.Getgocart, name='gocart'),
    path('cartdelete/<int:id>', views.Getcartdelete, name='cartdelete')
]
