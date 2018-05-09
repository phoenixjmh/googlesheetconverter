from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/table/')),
    path('search/',views.search, name = 'search'),
    path('table/',views.index, name = 'homepage'),
    path( 'search/table/', RedirectView.as_view(url = 'table/'))
]
