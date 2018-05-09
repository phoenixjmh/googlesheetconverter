

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from SheetApp import views
from django.views.generic import RedirectView
urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^table/$', views.index,name = 'homepage'),
    url(r'search/$',views.search),
    url('', RedirectView.as_view(url='/table/'))
]
