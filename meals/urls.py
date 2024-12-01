from django.urls import path
from .views import meal_list, delete_meal

urlpatterns = [
    path('', meal_list, name='meal_list'),
    path('delete/<int:meal_id>/', delete_meal, name='delete_meal'),
]
