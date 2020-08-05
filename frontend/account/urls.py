from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='account-index'),
    path('edit-profile', views.edit, name='account-edit'),
    path('update-profile', views.update, name='account-update'),
    path('edit-password', views.edit_pass, name='account-edit-pass'),
    path('sql-search', views.sqlsearch, name='account-sql-search'),
    path('sql-search-look', views.searchRequest, name='account-sql-search-look'),
    path('update-password', views.update_pass, name='account-update-pass'),
    path('change-profile-pic', views.profile_pic, name='account-profile-pic'),
    path('course-search', views.course_search, name='account-course-search'),
    path('search-course',  views.search_course,name='search-course-post')

]