from django.urls import path
from .import views
from .views import*




urlpatterns = [
    path('home/', homepage_view, name = 'home'),
    path('home2/', homepage2_view, name= 'home2'),
    path('about/', aboutpage_view, name = 'about'),
    path('contact/', contactuspage_view, name = 'contact'),
    path('signup/', signuppage_view, name = 'signup'),
    path('login/', loginpage_view, name = 'login'),
    path('logout/', logoutpage, name = 'logout'),
    path('store/',storepage_view, name = 'store'),
    path('cart/', cartpage_view, name = 'cart'),
    path('checkout/', checkoutpage_view, name ='checkout'),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]