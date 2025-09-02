from django.urls import path, include
from appTwo import views
from django.contrib import admin

urlpatterns = [
    path("", views.land, name="land"),
    path("index", views.index_ext, name="index"),
    path("other", views.other_ext, name="other"),
    path("list", views.show_list, name="web pages"),
    path("extension/", views.index, name="ext_index"),
    path("help", views.help, name="help"),
    path("forms", views.form_name_view, name="forms"),
    path("user", views.users, name="forms"),
    path("admin/", admin.site.urls, name="admin"),

]
