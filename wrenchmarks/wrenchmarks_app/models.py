from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	address = models.CharField(max_length=150)
	phone_number = models.CharField(max_length=12)
	email = models.EmailField(max_length=254)

	def get_absolute_url(self):
		return "/cust/%i" % self.id

class Vehicle(models.Model):
	customer = models.ForeignKey(Customer)
	vehicle_model = models.CharField(max_length=30)
	vehicle_make = models.CharField(max_length=30)
	vehicle_year = models.CharField(max_length=4)
	colour = models.CharField(max_length=20)
	plate = models.CharField(max_length=12)
	VIN = models.CharField(max_length=17)
	mileage = models.IntegerField()

	def get_absolute_url(self):
		return "/vehicle/%i" % self.id

class ServiceEvent(models.Model):
	vehicle = models.ForeignKey(Vehicle)
	service_date = models.DateField()
	service_description = models.CharField(max_length=80)
	service_mileage = models.IntegerField()

	def get_absolute_url(self):
		return "/service/%i" % self.id

class ServiceEventDetail(models.Model):
	service_event = models.ForeignKey(ServiceEvent)
	detail_description = models.CharField(max_length=200)
	technician = models.CharField(max_length=30)
	work_order = models.CharField(max_length=20)
	quantity = models.DecimalField(max_digits=5, decimal_places=2)
	unit_price = models.DecimalField(max_digits=8, decimal_places=2)

	def get_absolute_url(self):
		return "/servicedetail/%i" % self.id

class ServiceEventPart(models.Model):
	service_event = models.ForeignKey(ServiceEvent)
	part_description = models.CharField(max_length=200)
	technician = models.CharField(max_length=30)
	work_order = models.CharField(max_length=20)
	quantity = models.DecimalField(max_digits=5, decimal_places=2)
	unit_price = models.DecimalField(max_digits=8, decimal_places=2)

class Quote(models.Model):
	vehicle = models.ForeignKey(Vehicle)
	quote_date = models.DateField()
	quote_description = models.CharField(max_length=80)

	def get_absolute_url(self):
		return "/quote/%i" % self.id

class QuoteDetail(models.Model):
	quote = models.ForeignKey(Quote)
	quote_detail_description = models.CharField(max_length=200)
	quantity = models.DecimalField(max_digits=5, decimal_places=2)
	unit_price = models.DecimalField(max_digits=8, decimal_places=2)

	def get_absolute_url(self):
		return "/quotedetail/%i" % self.id

class QuotePart(models.Model):
	quote = models.ForeignKey(Quote)
	quote_part_description = models.CharField(max_length=200)
	quantity = models.DecimalField(max_digits=5, decimal_places=2)
	unit_price = models.DecimalField(max_digits=8, decimal_places=2)

