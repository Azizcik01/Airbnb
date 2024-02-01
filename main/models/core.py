from django.db import models
from django.utils.text import slugify


class Category(models.Model):

    title = models.CharField(verbose_name="Category name: ", max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    is_menu = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)
        
    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            'slug':self.slug,
        }
    
    def __str__(self) -> str:
        return f"{self.title}/{self.slug}"


class Product(models.Model):

    title = models.CharField(verbose_name="Product title: ", max_length=250)
    short_desc = models.CharField(verbose_name="Product short description: ", max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    seen_num = models.PositiveIntegerField(default=0)
    like_num = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title
    
    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            'description':self.short_desc,
            'seen_num':self.seen_num,
            'like_num':self.like_num,
            'category':self.category
        }


class Product_Images(models.Model):
    image = models.FileField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.product.title



