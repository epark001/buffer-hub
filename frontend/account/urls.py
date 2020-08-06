from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='account-index'),
    path('about-page', views.about_page, name='account-about'),

    path('edit-profile', views.edit, name='account-edit'),
    path('update-profile', views.update, name='account-update'),
    path('edit-password', views.edit_pass, name='account-edit-pass'),
    path('sql-search', views.sqlsearch, name='account-sql-search'),
    path('prof-search', views.profsearch, name='prof-sql-search'),
    path('sql-search-look', views.sqlsearchProf, name='prof-sql-search-look'),
    path('prof-search-look', views.searchRequest, name='account-sql-search-look'),
    path('update-password', views.update_pass, name='account-update-pass'),
    path('change-profile-pic', views.profile_pic, name='account-profile-pic'),
    path('course-search', views.course_search, name='account-course-search'),
    path('graduation-index', views.grad_reqs, name='graduation-reqs-forms'),
    path('search-course',  views.search_course,name='search-course-post'),
    path('add-graduation-course',  views.grad_course,name='add-grad-course-post'),
    path('course-insert', views.course_insert, name='account-course-insert'),
    path('prof-modal', views.prof_modal, name='prof-modal-post'),
    path('grad-req-insert', views.grad_req_insert, name='grad-req-insert-post'),
    path('grad-req-show', views.grad_req_show, name='grad-req-show-get'),
    path('grad-req-calc', views.grad_req_calc, name='grad-req-calc-post')
]