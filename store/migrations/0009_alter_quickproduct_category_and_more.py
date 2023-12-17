# Generated by Django 4.2.7 on 2023-12-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0008_quickproduct_delete_person"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quickproduct",
            name="category",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="quickproduct",
            name="product_image",
            field=models.ImageField(blank=True, null=True, upload_to="product_images/"),
        ),
        migrations.AlterField(
            model_name="quickproduct",
            name="quick_sale",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="quickproduct",
            name="unit",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
