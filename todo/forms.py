from .models import TodoModel
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'
        
        labels ={
            'subject':'',
            'details':'',
        }
        
        widgets = {
         'subject': forms.TextInput(attrs={'class': 'form-control bg-info rounded-5  p-3','rows': 2,'cols': 1,'placeholder': 'Enter Subjecct','id': 'id_content' }),
         'details': forms.Textarea(attrs={'class': 'form-control bg-info border-0 p-3','rows': 3,'cols': 1,'placeholder': 'Write Details','id': 'id_content' })
        }