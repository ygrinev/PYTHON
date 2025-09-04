from unicodedata import name
from django.urls import path, re_path
from . import views

app_name = 'basic_app'
urlpatterns = [
    path("", views.SchoolListView.as_view(), name='list'),
    re_path(r'(?P<pk>\d+)', views.SchoolDetailView.as_view(), name='detail')
]
