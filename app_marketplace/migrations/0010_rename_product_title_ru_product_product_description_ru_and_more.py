# Generated by Django 5.1.4 on 2025-01-10 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_marketplace', '0009_alter_order_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_title_ru',
            new_name='product_description_ru',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_title_uz',
            new_name='product_description_uz',
        ),
    ]
