# Generated by Django 4.0.6 on 2022-09-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0027_remove_test_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription_test',
            name='test_info_price',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
