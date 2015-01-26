from django.contrib import admin
from wrenchmarks_app.models import Customer, Vehicle, ServiceEvent, ServiceEventDetail, ServiceEventPart, Quote, QuoteDetail, QuotePart

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(ServiceEvent)
admin.site.register(ServiceEventDetail)
admin.site.register(ServiceEventPart)
admin.site.register(Quote)
admin.site.register(QuoteDetail)
admin.site.register(QuotePart)
 

# Register your models here.
