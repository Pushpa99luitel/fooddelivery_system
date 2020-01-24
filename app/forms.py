from django import forms
from app.models import User 
class UserForm(forms.FormModel):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
    model=User
	fields="_all_"

