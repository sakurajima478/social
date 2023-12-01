from django.urls import path

from .views import (
    posts_view,
)

app_name = 'blog'

urlpatterns = [
    path('', posts_view, name='posts'),
]
