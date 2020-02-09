from django.urls import path
from . import views

app_name = 'timeline'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),

    path('add/', views.create_post, name='create_post'),
]