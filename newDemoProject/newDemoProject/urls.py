
# newDemoProject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from project import views

from project import CollegeLink,StringEvaluation

urlpatterns = [
    path('admin/', admin.site.urls),    
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.home, name="home"),

    path('check-college-links', CollegeLink.link_check),
    path('string-evaluation', StringEvaluation.stringEvaluation),
]