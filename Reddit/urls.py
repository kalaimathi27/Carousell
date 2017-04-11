from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^track_votes/', views.track_votes, name='track_votes'),
    url(r'^add_title/', views.add_title, name='add_title'),
]