from django.urls import path, include
from . import views

urlpatterns = [
    path('account/',        include('frontend.account.urls')),
    path('',                views.index,        name='home-index'),
    path('signup/',         views.signup,       name='home-signup'),
    path('signup/post',     views.signup_post,  name='home-signup-post'),
    path('login/',          views.login,        name='home-login'),
    path('login/post',      views.login_post,   name='home-login-post'),
    path('logout/',         views.logout_post,  name='home-logout'),
    path('demo-insert/',    views.demo_insert,  name='demo-signup-post'),
    path('demo-query/',     views.demo_query,   name='demo-query-post'),
    path('demo-update/',    views.demo_update,  name='demo-update-post'),
    path('demo-delete/',    views.demo_delete,  name='demo-delete-post'),
    path('demo-site/',      views.demo_site,    name='demo-site-get'),
    path('get-user-info/',  views.get_user_info,name='get-user-info-post'),
    path('update-user/',    views.update_user,  name='update-user-post'),

]