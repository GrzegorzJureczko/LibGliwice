from django.urls import path

from . import views

app_name = 'demo'

urlpatterns = [
    path('libraries/generate', views.DemoVersion.as_view(), name='demo'),
]