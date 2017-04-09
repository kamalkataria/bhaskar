from django.contrib import admin
from fastfoods.models import *
# from fastfoods.models import Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_price', 'product_description', 'product_cat', 'product_image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'user_name', 'user_message', 'active_or_disable')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserComments, CommentAdmin)