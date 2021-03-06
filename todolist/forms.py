from django import forms
from django.forms import ModelForm
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=('title', 'description', "completed", "userId")
    
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter task...",
            }
        ),
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control form-control-lg",
                "rows":"3",
                "cols":"4",
                "placeholder": "Description..."
            }
        ),
    )

    completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "text-center"}),
    )

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=('title', 'description', "completed")
    
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter task...",
            }
        ),
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control form-control-lg",
                "rows":"3",
                "cols":"4",
                "placeholder": "Description..."
            }
        ),
    )

    completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "text-center"}),
    )

class RegistrForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='This field is required')
  
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', )