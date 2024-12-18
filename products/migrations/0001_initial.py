# Generated by Django 5.1.3 on 2024-12-13 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Care',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('care_name', models.CharField(max_length=20)),
                ('care_friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('user_friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('discount', models.IntegerField(blank=True, default=0)),
                ('discount_description', models.TextField()),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
                ('validity_start', models.DateTimeField()),
                ('validity_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light_name', models.CharField(max_length=20)),
                ('light_friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('species', models.CharField(blank=True, max_length=200)),
                ('product_description', models.TextField()),
                ('sale', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1020, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('pet_friendly', models.BooleanField(blank=True, default=False, null=True)),
                ('care_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.care')),
                ('category_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('light_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.light')),
            ],
        ),
    ]
