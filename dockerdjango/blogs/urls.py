from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.PostListView, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]
