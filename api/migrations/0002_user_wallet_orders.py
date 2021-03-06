# Generated by Django 4.0.2 on 2022-04-16 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wallet',
            field=models.FloatField(default=0, verbose_name='Wallet funds'),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Bought by:')),
                ('buyer_address', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.useraddress', verbose_name='Address')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.cardonsale', verbose_name='Product ID:')),
            ],
        ),
    ]
