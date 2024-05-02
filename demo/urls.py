from django.urls import path

from . import views

app_name = 'demo'

urlpatterns = [
    path('libraries/generate', views.DemoVersion.as_view(), name='demo'),
    path('dashboard/url-count/', views.UrlCountView.as_view(), name='url_count'),
]
