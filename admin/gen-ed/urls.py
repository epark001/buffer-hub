from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='gen-ed-add'),
    path('save/', views.save, name='gen-ed-save'),
    path('index/', views.index, name='gen-ed-index'),
    path('delete/<int:id>/', views.delete, name='gen-ed-delete'),
    path('edit/<int:id>/', views.edit, name='gen-ed-edit'),
    path('update/<int:id>/', views.update, name='gen-ed-update'),
]