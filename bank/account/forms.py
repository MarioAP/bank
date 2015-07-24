from django import forms
from django.contrib.auth.models import User

class AccountForm(forms.Form):
	user = forms.ModelChoiceField(queryset=User.objects.all())
	name = forms.CharField()
	amount = forms.FloatField()
	active = forms.BooleanField()
