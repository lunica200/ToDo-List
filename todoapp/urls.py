from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_first_category, name='first_category'),
    path('category/<slug:category_slug>/', views.show_category, name='category'),
    path('new-task/', views.CreateNewTask.as_view(), name='new_task'),
    path('edit-task/<int:pk>/', views.EditTask.as_view(), name='edit_task'),
    path('delete-task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
]
