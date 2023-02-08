from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Dish, WhyUs, Events, PhotoGallery, Chefs, Feedback

# Create your views here.

def main(request):
    categories = Category.object.all()
    dishes = Dish.object.all()
    for i in categories:
        for dish in i:
            print(dish)
            
    res_1 = f"Categories: {'; '.join(map(str, categories))}"
    res_2 = f"Dishes: {'; '.join(map(str, dishes))}"
    
    
    return HttpResponse(
        res_1 + '\n' + res_2
    )
    