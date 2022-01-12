from django.urls import path,include
from django.urls.conf import re_path
from .import views

app_name = "app"

urlpatterns = [
    path('',views.Article_list,name="article"),
    path('',views.Base,name="Base"),
    path('',views.Home,name="Home"),
    path('accounts/login/',views.Login,name="Login"),
    path('accounts/signup/',views.SignUp,name="SignUp"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.Contact,name="Contact"),
    path('article',views.Add_article,name="Add_article"),
    re_path('article-read/(?P<slug>[\w-]+)',views.Article_detail,name="detail"),
]