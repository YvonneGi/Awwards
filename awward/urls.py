from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^accounts/profile/(\d+)', views.profile, name = 'profile'),
    url(r'^new/project/', views.new_project, name = 'new-project'),
    url(r'^project/(\d+)', views.project, name = 'project'),
    url(r'^accounts/edit-profile/', views.edit_profile, name = 'edit-profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name='profile'),
    url(r'^api/project/$', views.ProjectList.as_view(),name='project')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)