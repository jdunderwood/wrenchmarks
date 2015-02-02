from django.conf.urls import patterns, include, url
from django.contrib import admin
from wrenchmarks_app.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wrenchmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', CustomerList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cust/(?P<customer_id>\d+)$', VehicleList.as_view()),
    url(r'^vehicle/(?P<pk>\d+)$', VehicleDetail.as_view()),
    url(r'^custedit/(?P<pk>\d+)$', CustomerUpdate.as_view()),
    url(r'^newcust$', CustomerCreate.as_view()),
    url(r'^custdelete/(?P<pk>\d+)$', CustomerDelete.as_view()),
    url(r'^newvehicle/(?P<customer_id>\d+)$', VehicleCreate.as_view()),
    url(r'^vehicleedit/(?P<pk>\d+)$', VehicleUpdate.as_view()),
    url(r'^vehicledelete/(?P<pk>\d+)$', VehicleDelete.as_view()),
    url(r'^service/(?P<pk>\d+)$', ServiceEventList.as_view()),
    url(r'^newservice/(?P<vehicle_id>\d+)$', ServiceEventCreate.as_view()),
    url(r'^serviceedit/(?P<pk>\d+)$', ServiceEventUpdate.as_view()),
    url(r'^servicedelete/(?P<pk>\d+)$', ServiceEventDelete.as_view()),
    url(r'^servicedetail/(?P<pk>\d+)$', ServiceDetailDetail.as_view()),
    url(r'^newservicedetail/(?P<service_event_id>\d+)$', ServiceDetailCreate.as_view()),
    url(r'^servicedetailedit/(?P<pk>\d+)$', ServiceDetailUpdate.as_view()),
    url(r'^servicedetaildelete/(?P<pk>\d+)$', ServiceDetailDelete.as_view()),
    url(r'^quote/(?P<pk>\d+)$', QuoteList.as_view()),
    url(r'^newquote/(?P<vehicle_id>\d+)$', QuoteCreate.as_view()),
    url(r'^quoteedit/(?P<pk>\d+)$', QuoteUpdate.as_view()),
    url(r'^quotedelete/(?P<pk>\d+)$', QuoteDelete.as_view()),
    url(r'^quotedetail/(?P<pk>\d+)$', QuoteDetailDetail.as_view()),
    url(r'^newquotedetail/(?P<quote_id>\d+)$', QuoteDetailCreate.as_view()),
    url(r'^quotedetailedit/(?P<pk>\d+)$', QuoteDetailUpdate.as_view()),
    url(r'^quotedetaildelete/(?P<pk>\d+)$', QuoteDetailDelete.as_view()),
    
)
