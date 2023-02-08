from django.contrib import admin
from .models import Category, Dish, WhyUs, Events, PhotoGallery, Chefs, Feedback

admin.site.register(PhotoGallery)
admin.site.register(WhyUs)
admin.site.register(Chefs)
admin.site.register(Feedback)
admin.site.register(Events)


class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    inlines = [DishAdmin]
    
@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish
    list_display = ['title', 'position', 'is_visible', 'ingredients', 
                    'description', 'price', 'photo', 'category', 'is_special']
    list_filter = ['category', 'is_special', 'is_visible']
    list_editable = ['position', 'is_visible','price']
    
