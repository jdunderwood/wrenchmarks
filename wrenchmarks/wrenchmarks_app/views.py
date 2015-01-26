from django.shortcuts import render
from wrenchmarks_app.forms import CustomerForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from wrenchmarks_app.models import Customer

# Create your views here.

class CustomerList(ListView):
	template_name = 'customer.html'
	model = Customer
