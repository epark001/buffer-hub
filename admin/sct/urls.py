from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='sct-add'),
    path('save/', views.save, name='sct-save'),
    path('index/', views.index, name='sct-index')
]