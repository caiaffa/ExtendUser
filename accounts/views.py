# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import UserForm, AccountForm
from .models import Account

class AccountCreate(generic.View):
	def get(self, request, *args, **kwargs):
		context = {'user_form':UserForm(), 'account_form':AccountForm()}
		return render(request, 'account/create.html', context)

	def post(self, request, *args, **kwargs):
		user_form = UserForm(request.POST, request.FILES)		
		account_form = AccountForm(request.POST, request.FILES)		
		if user_form.is_valid() and account_form.is_valid():
			user = user_form.save(commit=False)
			user.username = user_form.cleaned_data['email']			
			user.save()
			
			account = account_form.save(commit=False)
			account.user = user			
			account.save()
		context = {'user_form':user_form, 'account_form':account_form}
		return render(request, 'account/create.html', context)

account_create = AccountCreate.as_view()

class AccountCreate(generic.View):
	def get(self, request, *args, **kwargs):
		context = {'user_form':UserForm(), 'account_form':AccountForm()}
		return render(request, 'account/create.html', context)

	def post(self, request, *args, **kwargs):
		user_form = UserForm(request.POST, request.FILES)		
		account_form = AccountForm(request.POST, request.FILES)		
		if user_form.is_valid() and account_form.is_valid():
			user = user_form.save(commit=False)
			user.username = user_form.cleaned_data['email']			
			user.save()
			
			account = account_form.save(commit=False)
			account.user = user			
			account.save()
		context = {'user_form':user_form, 'account_form':account_form}
		return render(request, 'account/create.html', context)

account_create = AccountCreate.as_view()

class AccountEdit(generic.View):
	def get(self, request, pk=None, *args, **kwargs):
		account = get_object_or_404(Account, pk=pk)
		user = get_object_or_404(User, pk=account.user.pk)
		context = {'user_form':UserForm(instance=user), 'account_form':AccountForm(instance=account)}
		return render(request, 'account/edit.html', context)

	def post(self, request, pk=None, *args, **kwargs):
		account = get_object_or_404(Account, pk=pk)
		user = get_object_or_404(User, pk=account.user.pk)
		user_form = UserForm(request.POST, request.FILES, instance=user)		
		account_form = AccountForm(request.POST, request.FILES, instance=account)		
		if user_form.is_valid() and account_form.is_valid():
			user = user_form.save(commit=False)
			user.username = user_form.cleaned_data['email']			
			user.save()
			
			account = account_form.save(commit=False)
			account.user = user			
			account.save()
		context = {'user_form':user_form, 'account_form':account_form}
		return render(request, 'account/edit.html', context)

account_edit = AccountEdit.as_view()