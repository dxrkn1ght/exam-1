from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal

def meal_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        price = request.POST.get('price')
        type = request.POST.get('type')
        cuisine = request.POST.get('cuisine')
        Meal.objects.create(name=name, ingredients=ingredients, price=price, type=type, cuisine=cuisine)
        return redirect('meal_list')

    meals = Meal.objects.all()
    return render(request, 'meals/meal_list.html', {'meals': meals})

def delete_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    meal.delete()
    return redirect('meal_list')
