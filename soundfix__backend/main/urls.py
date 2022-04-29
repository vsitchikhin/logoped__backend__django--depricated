from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('12/', views.page, name='page'),
	path('main/', views.main, name='main')
]
