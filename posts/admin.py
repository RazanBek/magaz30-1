from django.contrib import admin

from posts.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'img']
    sortable_by = ('price', )
    list_display_links = ('id', 'name', )
    list_filter = ("price", )


admin.site.register(Category)
