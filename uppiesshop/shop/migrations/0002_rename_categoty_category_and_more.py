# Generated by Django 5.1.4 on 2024-12-12 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Categoty",
            new_name="Category",
        ),
        migrations.RenameIndex(
            model_name="category",
            new_name="shop_catego_name_289c7e_idx",
            old_name="shop_catego_name_1d3deb_idx",
        ),
    ]
