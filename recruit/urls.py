"""intershipcell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
     path('', views.index,name="index"),
     path('searchi', views.searchi,name="searchi"),
    path('IT_cat',views.IT_cat,name='IT_cat'),
    path('Mech_cat',views.Mech_cat,name='Mech_cat'),
    path('Ece_cat',views.Ece_cat,name='Ece_cat'),
    path('Mrk_cat',views.Mrk_cat,name='Mrk_cat'),
     path('detail_abt_internship/<int:id>/',views.detail_abt_internship,name='detail_abt_internship'),

     
    
    path('view_all_internships',views.view_all_internships,name='view_all_internships'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
