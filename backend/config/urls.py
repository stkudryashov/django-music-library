from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/library/', include('library.urls')),
]

admin.site.site_header = 'Music Library'
admin.site.site_title = 'Music Library'
