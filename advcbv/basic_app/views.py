from django.shortcuts import render
from django.views.generic import (View, TemplateView, 
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from . import models
from django.urls import reverse_lazy
# Create your views here.
class CBView(View):
  def get(self, request):
    return render(request, "index.html")
class IndexView(TemplateView):
  template_name = "index.html"
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    context["injected"] = "Basic Injection !"
    return context
class SchoolListView(ListView):
  context_object_name = 'schools'
  model = models.School
class SchoolDetailView(DetailView):
  context_object_name = 'school_detail'
  model = models.School
  template_name: 'basic_app/school_detail.html'
class SchoolCreateView(CreateView):
  # context_object_name = 'create_school'
  fields = ('name','principal','location')
  model = models.School
  # template_name: 'basic_app/school_form.html'
class SchoolUpdateView(UpdateView):
  # context_object_name = 'create_school'
  fields = ('name','principal')
  model = models.School
  # template_name: 'basic_app/school_form.html'
class SchoolDeleteView(DeleteView):
  # context_object_name = 'create_school'
  model = models.School
  # template_name: 'basic_app/school_form.html'
  success_url = reverse_lazy("basic_app:list")