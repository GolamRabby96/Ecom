# Generated by Django 2.1.2 on 2018-11-12 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('com_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('locations', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_model', models.CharField(max_length=255)),
                ('prince', models.FloatField()),
                ('description_one', models.TextField()),
                ('description_two', models.TextField()),
                ('image_one', models.ImageField(upload_to='C:\\Users\\win10\\Desktop\\prince\\ecom\\ecom\\media/')),
                ('image_two', models.ImageField(blank=True, upload_to='C:\\Users\\win10\\Desktop\\prince\\ecom\\ecom\\media/')),
                ('image_three', models.ImageField(blank=True, upload_to='C:\\Users\\win10\\Desktop\\prince\\ecom\\ecom\\media/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Brand')),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.SubCategory'),
        ),
        migrations.AddField(
            model_name='payment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Product'),
        ),
        migrations.AddField(
            model_name='brand',
            name='cat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Category'),
        ),
        migrations.AddField(
            model_name='brand',
            name='sub_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.SubCategory'),
        ),
    ]
