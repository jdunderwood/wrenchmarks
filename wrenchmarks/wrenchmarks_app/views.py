from django.shortcuts import render, get_object_or_404
from wrenchmarks_app.forms import CustomerForm
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from wrenchmarks_app.models import Customer, Vehicle

# Create your views here.

class CustomerList(ListView):
	template_name = 'customer_list.html'
	model = Customer

class VehicleList(ListView):
	template_name = 'customer_vehicles.html'

	def get_queryset(self):
		return Vehicle.objects.filter(customer_id=self.kwargs.get("customer_id", None))

class VehicleDetail(DetailView):
	template_name = 'vehicle_detail.html'
	model = Vehicle
