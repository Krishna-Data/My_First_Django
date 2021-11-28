from django.conf.urls import url
from my_first_app import views

urlpatterns = [
    url('^$',views.index,name='index'),
]
