"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
     url(r'^$', views.awwards, name = 'Awwards'),
     url(r'^projects/(\d+)',views.projects_of_day,name ='project'),
     url(r'^new/profile', views.new_profile, name='new-profile'),
     url(r'^new/view_profile', views.view_profile, name='view_profile'),
    #  url(r'^new/view_profile$', views.view_profile, name='view_profile'),
     url(r'^new/project', views.postproject, name='postproject'),
     url(r'^ajax/projectletter/$', views.projectletter, name='projectletter'),

     url(r'^api/project/$', views.ProjectList.as_view()),

     url(r'^api/profile/$', views.ProfileList.as_view()),

    url(r'^api-token-auth/', obtain_auth_token),
     url(r'^search/', views.search_results, name='search_results'),
    # url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',
    # views.MerchDescription.as_view())

     ]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)