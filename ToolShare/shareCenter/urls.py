from django.conf.urls import patterns, url
from shareCenter import views

urlpatterns = patterns('',
    # Add tool URL 
    url(r'^addtool', views.addTool, name='addtool' ),
        
    # User directory
    url(r'^userdirectory', views.userDirectory, name='userdirectory'),
    
    # Add tool/toolid URL, used for pass tool id for redirect messages 
    url(r'^tool/(?P<tool_id>\d+)', views.toolInfo, name='tool'),
    
    # User profile URL
    url(r'^user/(?P<username>\w+)', views.userProfile, name='username'),
    
    # Deleting tools
    url(r'^tool/delete/(?P<tool_id>\d+)', views.deleteTool, name='deletetool'),
    
    # editing tools
    url(r'^tool/edit/(?P<tool_id>\d+)', views.editTool, name='edittool'),

    # editing tools
    url(r'^tool/changestate/(?P<tool_id>\d+)', views.changeToolState, name='changeToolState'),

    #editing user info
    url(r'^edituser/(?P<username>\w+)', views.editUserInfo, name='edituserinfo'),
    
    #editing user info
    url(r'^editpassword', views.editPassword, name='editpassword'),
    
    #create a shed
    url(r'^createshed', views.createShed, name='createshed'),
    
    #view for a shed
    url(r'^shed/(?P<username>\w+)', views.shed, name='shed'),
    
    #shed list
    url(r'^shedlist', views.shedList, name='shedlist'),

    #Delete Shed
    url(r'^deleteshed', views.deleteShed, name='deleteshed'),
)
