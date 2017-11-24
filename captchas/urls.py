from captchas import views
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^prueba/$',views.index,name='index')
]

