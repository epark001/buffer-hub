from django.urls import path, include
from . import views
import uuid
urlpatterns = [
    path('add/', views.add, name='sct-add'),
    path('save/', views.save, name='sct-save'),
    path('index/', views.index, name='sct-index'),
    path('index-user/', views.index_user, name='sct-index-user'),
    path('save-user/', views.save_user, name='sct-save-user'),
    path('delete/<uuid:id>/', views.delete, name='sct-delete'),
]