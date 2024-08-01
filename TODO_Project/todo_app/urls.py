from django.urls import path
from .views import add_task, show_task, update_details, delete_details


urlpatterns = [
    path('add/', add_task, name='add_url'),
    path('show/', show_task, name='show_url'),
    path('update/<int:pk>/', update_details, name='update_url'),
    path('delete/<int:pk>/', delete_details, name='delete_url')
]