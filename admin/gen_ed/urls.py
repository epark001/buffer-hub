from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='gen_ed-add'),
    path('save/', views.save, name='gen_ed-save'),
    path('index/', views.index, name='gen_ed-index')
]