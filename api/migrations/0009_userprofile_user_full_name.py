# Generated by Django 4.0.2 on 2022-03-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_useraddress_remove_cardonsale_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_full_name',
            field=models.CharField(default='name', max_length=254, verbose_name='Full name'),
        ),
    ]
