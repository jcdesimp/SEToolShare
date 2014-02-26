from django.conf.urls import patterns, url
from messageCenter import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ToolShare.views.home', name='home'),
    url(r'^$', views.inboxView, name='messageCenter' ),
    url(r'^sendMessage/(?P<user_id>\d+)', views.sendMessage, name='sendMessage'),
    url(r'^message/(?P<message_id>\d+)', views.messageView, name='viewMessage'),
    url(r'^delete/(?P<message_id>\d+)', views.deleteMessage, name='viewMessage'),
    url(r'^sendrequest/(?P<toolId>\d+)', views.sendToolRequest, name='sendRequest'),
    url(r'^approverequest/(?P<message_id>\d+)/(?P<toolId>\d+)', views.approveRequest, name='approveRequest'),
    url(r'^reservations/delete/(?P<reservation_id>\d+)', views.deleteReservation, name='deleteReservation'),
    url(r'^reservations/return/(?P<reservation_id>\d+)', views.returnReservation, name='returnReservation'),
    url(r'^reservations/', views.myReservations, name='myreservations'),
    
)
