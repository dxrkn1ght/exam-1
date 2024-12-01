from django.urls import path
from .views import taxi_list, delete_taxi

urlpatterns = [
    path('', taxi_list, name='taxi_list'),
    path('delete/<int:taxi_id>/', delete_taxi, name='delete_taxi'),
]
