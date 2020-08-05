from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='student_misc-add'),
    path('save/', views.save, name='student_misc-save'),
    path('index/', views.index, name='student_misc-index')
]