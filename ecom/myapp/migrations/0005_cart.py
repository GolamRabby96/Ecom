# Generated by Django 2.1.2 on 2018-11-17 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20181116_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Product')),
            ],
        ),
    ]
