from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='gpa_table-add'),
    path('save/', views.save, name='gpa_table-save'),
    path('index/', views.index, name='gpa_table-index')
]