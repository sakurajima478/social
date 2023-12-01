from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

from .views import (
    register_view,
    login_view,
    logout_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('', include('blog.urls', namespace='blog')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)