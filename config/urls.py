from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search_for_things.urls')),
    path('api/', include('search_for_things.api.urls')),
]
