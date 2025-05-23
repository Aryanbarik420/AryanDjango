"""
URL configuration for studentresult project.

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
from django.contrib import admin
from django.urls import path
from Result.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("add_temp/",add_student_template),
    path("add/",add_student),
    path("update_temp/",update_student_template),
    path('update/',update_student),
    path("delete_temp",delete_student_template),
    path('delete/',delete_student),
    path("findresult_temp/",find_result_template),
    path("findresult/",find_result),
    path("view/",view_student),
]
