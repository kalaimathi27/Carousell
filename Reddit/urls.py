from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.FakeReddit().index, name='index'),
    url(r'^track_votes/', views.FakeReddit().track_votes, name='track_votes'),
    url(r'^add_title/', views.FakeReddit().add_title, name='add_title'),
]