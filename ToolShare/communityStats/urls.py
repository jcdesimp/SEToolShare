from django.conf.urls import patterns, url
from communityStats import views

urlpatterns = patterns('',
    # Add tool URL 
    url(r'^stats', views.statReport, name='stats' ),
    
    )