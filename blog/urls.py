from django.urls import path
from blog.views import (
    blog_create_view,
    detail_blog_view,
    edit_blog_view,
)

app_name = 'blog'

urlpatterns = [
    path('create/', blog_create_view, name='create'),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit', edit_blog_view, name="edit"),
]