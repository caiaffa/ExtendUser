# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birth_date = models.DateField(null=True, blank=True)

	class Meta:
		verbose_name = 'Conta'
		verbose_name_plural = 'Contas'
