# Generated by Django 4.0.6 on 2022-09-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_admin', '0002_clinical_laboratory_technician_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Information',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(blank=True, max_length=200, null=True)),
                ('test_price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
