from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('super_cars.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
