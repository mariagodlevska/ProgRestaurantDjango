from django.contrib import admin
from .models import Category, Dish, WhyUs, Events, PhotoGallery, Chefs, Feedback

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(PhotoGallery)
admin.site.register(WhyUs)
admin.site.register(Chefs)
admin.site.register(Feedback)
admin.site.register(Events)


class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']
    


