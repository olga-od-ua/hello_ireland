# Generated by Django 3.2.9 on 2021-12-23 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0002_alter_favouriteproductslist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favouriteproduct',
            name='date_added',
        ),
    ]
