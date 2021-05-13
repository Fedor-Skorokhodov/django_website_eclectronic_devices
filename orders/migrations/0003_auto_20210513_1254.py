# Generated by Django 3.2.1 on 2021-05-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_in_process',
            field=models.BooleanField(default=False),
        ),
    ]