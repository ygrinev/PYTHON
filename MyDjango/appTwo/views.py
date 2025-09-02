from django.shortcuts import render
from appTwo.models import AccessRecord, Topic, WebPage
from appTwo.forms import NewUserForm
from . import forms
# Create your views here.
def index(request):
    my_dict = {'dog':"dog_against_straus.JPG"}
    return render(request,'dog.html',context=my_dict)
    # return HttpResponse('<h1><em>My Second App</em></h1>')
def help(request):
    my_dict = {'copyright':"All rights reserved!"}
    return render(request,'help.html',context=my_dict)
def show_list(request):
    webpages_list = AccessRecord.objects.order_by('date')
    my_dict = {'access_records': webpages_list}
    return render(request,'web_pages.html',context=my_dict)
def form_name_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Validation successful!')
            print(f'Name = {form.cleaned_data['name']}')
            print(f'Email = {form.cleaned_data['email']}')
            print(f'Text = {form.cleaned_data['text']}')
    return render(request,'form_page.html',context={'form':form})
def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            print('Validation successful!')
            print(f'Name = {form.cleaned_data['first_Name']}')
            print(f'Name = {form.cleaned_data['last_Name']}')
            print(f'Email = {form.cleaned_data['email']}')
            form.save(commit=True)
            return show_list(request)
    return render(request,'users.html',context={'form':form})
def land(request):
    return render(request,'base.html')
def index_ext(request):
    return render(request,'children/index.html')
def other_ext(request):
    return render(request,'children/other.html')
