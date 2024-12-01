from django.shortcuts import render, redirect, get_object_or_404
from .models import Taxi

def taxi_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        license_plate = request.POST.get('license_plate')
        driver_name = request.POST.get('driver_name')
        capacity = request.POST.get('capacity')
        model = request.POST.get('model')
        status = request.POST.get('status')
        Taxi.objects.create(name=name, license_plate=license_plate, driver_name=driver_name, capacity=capacity, model=model, status=status)
        return redirect('taxi_list')

    taxis = Taxi.objects.all()
    return render(request, 'taxi/taxi_list.html', {'taxis': taxis})

def delete_taxi(request, taxi_id):
    taxi = get_object_or_404(Taxi, id=taxi_id)
    taxi.delete()
    return redirect('taxi_list')
