from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url('^', include('django.contrib.auth.urls')),
]
