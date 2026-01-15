from django.urls import path
from Blogs.views import *
from . import views



urlpatterns = [
    path('', homepage_view, name = 'home'),
    path('home2/', home2page_view, name = 'home2'),
    path('about/', aboutpage_view, name = 'about'),
    path('signup/', signuppage_view, name ='signup'),
    path('login/', loginpage_view, name = 'login'),
    path('logout/', logoutpage_view, name = 'logout'),
    path('profile/', profilepage_view, name = 'profile'),
    path('update_profile/', updateprofilepage_view, name = 'update_profile'),
    path('blogspostsshow/', blogspostsshowpagelist_view.as_view(), name = 'blogspostsshow'),
    path('blogsdetailshow/<int:pk>/', blogsdetailshowpagelist_view.as_view(), name = 'blogsdetailshow'),
    path('create_blogs/', createblogspage_view.as_view(), name = 'create_blogs'),
    path('blogsdetailshow/<int:pk>/update/', updateblogspage_view.as_view(), name = 'updateblogs'),
    path('blogsdetailshow/<int:pk>/delete/', deleteblogspage_view.as_view(), name = 'deleteblogs'),
]