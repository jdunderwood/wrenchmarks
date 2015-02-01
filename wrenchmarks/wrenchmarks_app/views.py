from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from wrenchmarks_app.forms import CustomerForm
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from wrenchmarks_app.models import Customer, Vehicle

# Create your views here.

class CustomerList(ListView):
	template_name = 'customer_list.html'
	model = Customer

class CustomerUpdate(UpdateView):
	model = Customer
	fields = ['first_name', 'last_name', 'address', 'phone_number', 'email']
	template_name = 'customer_update.html'
	
class CustomerCreate(CreateView):
	model = Customer
	fields = ['first_name', 'last_name', 'address', 'phone_number', 'email']
	template_name = 'customer_create.html'

class CustomerDelete(DeleteView):
	model = Customer
	template_name = 'customer_delete_confirm.html'
	success_url = '/'

class VehicleList(ListView):
	template_name = 'customer_vehicles.html'

	def get_context_data(self, **kwargs):
		context = super(VehicleList, self).get_context_data(**kwargs)
		context['customer_detail'] = Customer.objects.get(id=self.kwargs.get("customer_id", None))
		return context

	def get_queryset(self):
		return Vehicle.objects.filter(customer_id=self.kwargs.get("customer_id", None))

class VehicleDetail(DetailView):
	template_name = 'vehicle_detail.html'
	model = Vehicle

class VehicleCreate(CreateView):
	model = Vehicle
	fields = ['vehicle_year', 'vehicle_make', 'vehicle_model', 'colour', 'plate', 'VIN', 'mileage']
	template_name = 'vehicle_create.html'

	def form_valid(self, form):
		vehicle = form.save(commit=False)
		vehicle.customer_id = self.kwargs.get("customer_id", None)
		vehicle.save()
		return HttpResponseRedirect(self.get_success_url())
