# Generated by Django 5.1 on 2024-09-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_product_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="public",
            field=models.BooleanField(default=True),
        ),
    ]
