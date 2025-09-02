from tkinter.ttk import Widget
from django import forms
from django.core import validators

from appTwo.models import User

class FormName(forms.Form):
  name = forms.CharField()
  email = forms.EmailField(validators=[validators.EmailValidator])
  verify_email = forms.EmailField(label="Enter email again:", validators=[validators.EmailValidator])
  text = forms.CharField(widget=forms.Textarea)
  # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
  def clean(self):
    all_data = super().clean()
    if all_data['email'].lower() != all_data['verify_email'].lower():
      raise forms.ValidationError('Email should match!')

class NewUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = '__all__'