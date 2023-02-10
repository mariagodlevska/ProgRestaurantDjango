from django.shortcuts import render
from .models import Category, Dish, WhyUs, Events, PhotoGallery, Chefs, Feedback


def main(request):
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.all()
    whyus = WhyUs.objects.all()
    events = Events.objects.all()
    photogallery = PhotoGallery.objects.all()
    chefs = Chefs.objects.all()
    feedback = Feedback.objects.all()
            
    return render(request, 'index.html', context={
            'categories': categories,
            'dishes': dishes,
            'whyus': whyus,
            'events': events,
            'photogallery': photogallery,
            'chefs': chefs,
            'feedback': feedback         
        })
    