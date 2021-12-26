# Generated by Django 3.2.9 on 2021-12-26 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_alter_productreview_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
