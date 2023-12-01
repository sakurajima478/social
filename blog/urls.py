from django.urls import path

from .views import (
    posts_view,
    like,
)

app_name = 'blog'

urlpatterns = [
    path('', posts_view, name='posts'),
    
    path('like/<int:pk>', like, name='like')
]
