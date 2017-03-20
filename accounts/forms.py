# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from .models import Account


class UserForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class AccountForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(AccountForm, self).__init__(*args, **kwargs)
		self.fields['birth_date'].required = True

	class Meta:
		model = Account
		fields = ('birth_date',)