# Generated by Django 4.0.5 on 2022-06-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_item_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.CharField(choices=[('bakery', 'bakery'), ('meat&seafood', 'meat&seafood'), ('fruits', 'fruits'), ('vegetables', 'vegetables'), ('dairy', 'dairy')], default=None, max_length=100),
        ),
    ]