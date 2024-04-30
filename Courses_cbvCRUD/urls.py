"""
URL configuration for Courses_cbvCRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from crudCoursesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('create/', views.CourseCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.CourseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view(), name='delete'),
]
