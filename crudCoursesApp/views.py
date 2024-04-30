from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from crudCoursesApp.models import Course



# Create your views here.
class CourseListView(ListView):
    model = Course
    #Default template name is course_list.html (model_list)

class CourseDetailView(DetailView):
    model = Course
    #model_detail with id -

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    #Default template name is course_form.html ( model_form)

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses')


