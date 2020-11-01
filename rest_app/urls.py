from django.urls import path, include
from . import views

urlpatterns = [  
    path('', views.showHome,name='home'),
    path('video/', views.process_form,name='video'),
]
