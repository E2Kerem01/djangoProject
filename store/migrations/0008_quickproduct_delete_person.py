# Generated by Django 4.2.7 on 2023-12-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0007_person"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuickProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=255)),
                ("stock_quantity", models.IntegerField()),
                ("cost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("selling_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("unit", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
                ("quick_sale", models.CharField(max_length=50)),
                ("kdv_rate", models.DecimalField(decimal_places=2, max_digits=5)),
                ("product_image", models.ImageField(upload_to="product_images/")),
            ],
        ),
        migrations.DeleteModel(
            name="Person",
        ),
    ]
