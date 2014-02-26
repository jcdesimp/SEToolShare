from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
    # Login URL 
    url(r'^$', views.loginUser, name='login' ),
    url(r'^home', views.home, name='home' ),
    url(r'^credits', views.credits, name='credits' )
)
