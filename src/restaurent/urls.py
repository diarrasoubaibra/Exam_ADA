"""
URL configuration for cantine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views.menu_views import *
from .views.plat_views import *

app_name = 'restaurent'
urlpatterns = [
    # menu urls
    path('', menu_list, name='menu_list'),
    path('menu/add', menu_form, name='menu_add'),
    path('menu/update/<int:id>', menu_form, name='menu_edit'),
     path('menu/<int:id>/delete/', menu_delete, name='menu_delete'),

    # Plat Urls
    path('plat/list', plat_list, name='plat_list'),
    path('plat/add', plat_form, name='plat_add'),
    path('plat/<int:id>/update', plat_form, name='plat_edit'),
    path('plat/<int:id>/delete/', plat_delete, name='plat_delete'),

]
