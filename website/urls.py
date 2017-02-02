from django.conf.urls import url,include

from . import views

app_name='website'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^new/', views.form_data, name='new'),
]
