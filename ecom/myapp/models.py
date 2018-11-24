from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import math
# Create your models here.

class Customer(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    locations = models.TextField()

    def __str__(self):
        return self.name.username


class Category(models.Model):
    cat_name=models.CharField(max_length=255)

    def __str__(self):
        return self.cat_name

class SubCategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Brand(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_model = models.CharField(max_length=255)
    prince = models.FloatField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    image_one = models.ImageField(upload_to='media/profile_pics')
    image_two = models.ImageField(upload_to='media/profile_pics',blank=True)
    image_three = models.ImageField( upload_to='media/profile_pics' ,blank=True)
    product_rating = models.IntegerField(blank=True, null=True)

    topic_one = models.CharField(blank=True, null=True, max_length=255)
    description_one = models.TextField(blank=True, null=True)

    topic_two = models.CharField(blank=True, null=True, max_length=255)
    description_two = models.TextField(blank=True, null=True)

    topic_three = models.CharField(blank=True, null=True, max_length=255)
    description_three = models.TextField(blank=True, null=True)

    topic_four = models.CharField(blank=True, null=True, max_length=255)
    description_four = models.TextField(blank=True, null=True)

    topic_five = models.CharField(blank=True, null=True, max_length=255)
    description_five = models.TextField(blank=True, null=True)

    topic_six = models.CharField(blank=True, null=True, max_length=255)
    description_six = models.TextField(blank=True, null=True)

    topic_seven = models.CharField(blank=True, null=True, max_length=255)
    description_seven = models.TextField(blank=True, null=True)

    topic_eight = models.CharField(blank=True, null=True, max_length=255)
    description_eight = models.TextField(blank=True, null=True)

    topic_nine = models.CharField(blank=True, null=True, max_length=255)
    description_nine = models.TextField(blank=True, null=True)

    topic_ten = models.CharField(blank=True, null=True, max_length=255)
    description_ten = models.TextField(blank=True, null=True)

    topic_eleven = models.CharField(blank=True, null=True, max_length=255)
    description_eleven = models.TextField(blank=True, null=True)

    topic_twelve = models.CharField(blank=True, null=True, max_length=255)
    description_twelve = models.TextField(blank=True, null=True)

    topic_therteen = models.CharField(blank=True, null=True, max_length=255)
    description_therteen = models.TextField(blank=True, null=True)

    topic_therteen = models.CharField(blank=True, null=True, max_length=255)
    description_therteen = models.TextField(blank=True, null=True)

    topic_flourteen = models.CharField(blank=True, null=True, max_length=255)
    description_flourteen = models.TextField(blank=True, null=True)

    topic_fifteen = models.CharField(blank=True, null=True, max_length=255)
    description_fifteen = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product_model

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.CharField(max_length=255)
    comment = models.TextField()
    rating = models.IntegerField(null=False, blank=False)
    com_date = models.DateTimeField(auto_now=False, auto_now_add=True)



    def calculate_rating(self, id):
        contex = Product.objects.get(id=id)
        catch = Comment.objects.filter(product=contex.id)
        cot = Comment.objects.filter(product=contex.id).count()
        total = 0
        for con in catch:
            total = total + con.rating
            sum=(total/cot)
        number=math.ceil(sum)
        contex.product_rating=number
        contex.save()


    def __str__(self):
        return self.customer


class Payment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payment


class cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.date
