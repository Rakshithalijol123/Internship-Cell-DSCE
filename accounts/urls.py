from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('logout',views.logout,name='logout'),
    path('inter',views.inter,name='inter'),
    path('info_me/',views.info_me,name='info_me'),
    path('resume',views.resume,name='resume'),
]