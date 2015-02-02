from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from wrenchmarks_app.forms import CustomerForm
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from wrenchmarks_app.models import *

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

	def get_context_data(self, **kwargs):
		context = super(VehicleDetail, self).get_context_data(**kwargs)
		context['service_events'] = ServiceEvent.objects.filter(vehicle_id=self.kwargs.get("pk", None))
		context['quotes'] = Quote.objects.filter(vehicle_id=self.kwargs.get("pk", None))
		return context

class VehicleCreate(CreateView):
	model = Vehicle
	fields = ['vehicle_year', 'vehicle_make', 'vehicle_model', 'colour', 'plate', 'VIN', 'mileage']
	template_name = 'vehicle_create.html'

	def form_valid(self, form):
		vehicle = form.save(commit=False)
		vehicle.customer_id = self.kwargs.get("customer_id", None)
		vehicle.save()
		return HttpResponseRedirect('/cust/' + self.kwargs.get("customer_id", None))

class VehicleUpdate(UpdateView):
	model = Vehicle
	fields = ['vehicle_year', 'vehicle_make', 'vehicle_model', 'colour', 'plate', 'VIN', 'mileage']
	template_name = 'vehicle_update.html'

class VehicleDelete(DeleteView):
	model = Vehicle
	template_name = 'vehicle_delete_confirm.html'

	def get_success_url(self):
		return '/cust/' + str(Vehicle.objects.get(id=self.kwargs.get("pk", None)).customer_id)

class ServiceEventList(ListView):
	model = ServiceEventDetail
	template_name = 'vehicle_service.html'

	def get_context_data(self, **kwargs):
		context = super(ServiceEventList, self).get_context_data(**kwargs)
		context['service_event'] = ServiceEvent.objects.get(id=self.kwargs.get("pk", None))
		return context

	def get_queryset(self):
		return ServiceEventDetail.objects.filter(service_event_id=self.kwargs.get("pk", None))

class ServiceEventCreate(CreateView):
	model = ServiceEvent
	fields = ['service_date', 'service_description', 'service_mileage']
	template_name = 'service_event_create.html'

	def form_valid(self, form):
		service_event = form.save(commit=False)
		service_event.vehicle_id = self.kwargs.get("vehicle_id", None)
		service_event.save()
		return HttpResponseRedirect('/service/' + str(service_event.id))	
	
class ServiceEventUpdate(UpdateView):
	model = ServiceEvent
	fields = ['service_date', 'service_description', 'service_mileage']
	template_name = 'service_event_update.html'

class ServiceEventDelete(DeleteView):
	model = ServiceEvent
	template_name = 'service_event_delete_confirm.html'

	def get_success_url(self):
		return '/vehicle/' + str(ServiceEvent.objects.get(id=self.kwargs.get("pk", None)).vehicle_id)

class ServiceDetailDetail(DetailView):
	model = ServiceEventDetail
	template_name = 'service_detail.html'

class ServiceDetailUpdate(UpdateView):
	model = ServiceEventDetail
	fields = ['detail_description', 'technician', 'work_order', 'quantity', 'unit_price']
	template_name = 'service_event_detail_update.html'

class ServiceDetailCreate(CreateView):	
	model = ServiceEventDetail
	fields = ['detail_description', 'technician', 'work_order', 'quantity', 'unit_price']
	template_name = 'service_event_detail_create.html'

	def form_valid(self, form):
		service_event_detail = form.save(commit=False)
		service_event_detail.service_event_id = self.kwargs.get("service_event_id")
		service_event_detail.save()
		return HttpResponseRedirect('/service/' + str(self.kwargs.get("service_event_id")))

class ServiceDetailDelete(DeleteView):
	model = ServiceEventDetail
	template_name = 'service_event_detail_delete.html'


class QuoteList(ListView):
	model = QuoteDetail
	template_name = 'vehicle_quote.html'

	def get_context_data(self, **kwargs):
		context = super(QuoteList, self).get_context_data(**kwargs)
		context['quote'] = Quote.objects.get(id=self.kwargs.get("pk", None))
		return context

	def get_queryset(self):
		return QuoteDetail.objects.filter(quote_id=self.kwargs.get("pk", None))

class QuoteCreate(CreateView):
	model = Quote
	fields = ['quote_description', 'quote_date']
	template_name = 'quote_create.html'

	def form_valid(self, form):
		quote = form.save(commit=False)
		quote.vehicle_id = self.kwargs.get("vehicle_id", None)
		quote.save()
		return HttpResponseRedirect('/quote/' + str(quote.id))	
	
class QuoteUpdate(UpdateView):
	model = Quote
	fields = ['quote_description', 'quote_date']
	template_name = 'quote_update.html'

class QuoteDelete(DeleteView):
	model = Quote
	template_name = 'quote_delete_confirm.html'

	def get_success_url(self):
		return '/vehicle/' + str(Quote.objects.get(id=self.kwargs.get("pk", None)).vehicle_id)

class QuoteDetailDetail(DetailView):
	model = QuoteDetail
	template_name = 'quote_detail.html'

class QuoteDetailUpdate(UpdateView):
	model = QuoteDetail
	fields = ['quote_detail_description', 'quantity', 'unit_price']
	template_name = 'quote_detail_update.html'

class QuoteDetailCreate(CreateView):	
	model = QuoteDetail
	fields = ['quote_detail_description', 'quantity', 'unit_price']
	template_name = 'quote_detail_create.html'

	def form_valid(self, form):
		quote_detail = form.save(commit=False)
		quote_detail.quote_id = self.kwargs.get("quote_id")
		quote_detail.save()
		return HttpResponseRedirect('/quote/' + str(self.kwargs.get("quote_id")))

class QuoteDetailDelete(DeleteView):
	model = QuoteDetail
	template_name = 'quote_detail_delete.html'
