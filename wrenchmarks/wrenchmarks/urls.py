from django.conf.urls import patterns, include, url
from django.contrib import admin
from wrenchmarks_app.views import CustomerList, VehicleList, VehicleDetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wrenchmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', CustomerList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cust/(?P<customer_id>\d+)$', VehicleList.as_view()),
    url(r'^vehicle/(?P<pk>\d+)$', VehicleDetail.as_view()),
)
