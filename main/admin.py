from django.contrib import admin
from main.models import User, Product, Category, Product_Images


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Product_Images)

