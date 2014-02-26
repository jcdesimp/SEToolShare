from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from login.views import logoutUser, home
from shareCenter.views import toolDirectory
from login.views import home
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ToolShare.views.home', name='home'),
    # url(r'^ToolShare/', include('ToolShare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    url(r'^registration/', include('registration.urls', namespace='registration')),
    url(r'^login/', include('login.urls', namespace='login')),
    url(r'^logout/', logoutUser),
    url(r'^home/', home),
    url(r'^sharecenter/', include('shareCenter.urls', namespace='sharecenter')),
    url(r'^tooldirectory/', toolDirectory),
    url(r'^messagecenter/', include('messageCenter.urls', namespace='messagecenter')),
    url(r'^communitystats/', include('communityStats.urls', namespace='communitystats')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'SITE_ROOT': 'static'}),
    
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()