# Generated by Django 3.2.9 on 2021-12-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_size',
            field=models.CharField(blank=True, db_column='product_size', max_length=4, null=True),
        ),
    ]
