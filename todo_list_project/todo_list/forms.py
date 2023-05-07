from django import forms  
from todo_list.models import TodoTask 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TodoTaskForm(forms.ModelForm):  
    class Meta:  
        model = TodoTask  
        fields = ['title', 'description', 'duedate', 'complete'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'title': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'description': forms.Textarea(attrs={ 'class': 'form-control rounded-0','rows':'5' }),
            'duedate': forms.DateInput(attrs={ 'class': 'form-control','type' : 'date' }),
            'complete':forms.CheckboxInput(attrs={ 'class': 'form-check-input me-2' }),
      }

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']