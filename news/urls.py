from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.news_of_day, name='newsToday'),
    url('^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name='pastNews'),
    url('^search/$', views.search_results, name='search_results')
]