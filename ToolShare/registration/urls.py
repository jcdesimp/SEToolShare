from django.conf.urls import patterns, url
from registration import views

urlpatterns = patterns('',
    # registration URL                     
    url(r'^$', views.register, name='registration' ),
)
