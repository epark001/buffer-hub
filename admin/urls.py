from django.urls import path, include

urlpatterns = [
    path('', include('admin.login.urls')),
    path('dashboard/', include('admin.dashboard.urls')),
    path('users/', include('admin.user.urls')),
    path('gpa_table/', include('admin.gpa_table.urls')),
    path('homepage/', include('admin.homepage.urls')),
]