# Generated by Django 4.0.2 on 2022-05-09 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_orders_customer_alter_orders_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='shipping_fee',
            field=models.IntegerField(blank=True, default=5, null=True, verbose_name='Shipping fee'),
        ),
    ]
