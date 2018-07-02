from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from users.views import login_error

urlpatterns = [
    path('admin/error', login_error),
    path('admin/', admin.site.urls),
    path('', include(('social_django.urls', 'social'), namespace='social')),
]
