from django import forms
from django.forms import ModelForm
from .models import BlogContent


class testForm(forms.Form):
    Name=forms.CharField(max_length=100)
    ROll_no=forms.IntegerField()
    school=forms.CharField(max_length=100)

class ModelsDemoForm(ModelForm):
    class Meta:
        model = BlogContent

        fields = '__all__'

        


    