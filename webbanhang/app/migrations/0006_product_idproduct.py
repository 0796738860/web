# Generated by Django 5.0.6 on 2024-06-23 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='idproduct',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
