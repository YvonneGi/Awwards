from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^accounts/profile/(\d+)', views.profile, name = 'profile'),
    url(r'^new/project/', views.new_project, name = 'new-project'),
    url(r'^accounts/edit-profile/', views.edit_profile, name = 'edit-profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/project/', views.new_project, name = 'new-project'),
    url(r'^api/merch/$', views.ProfileList.as_view()),
    url(r'^api/merch/$', views.ProjectList.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)