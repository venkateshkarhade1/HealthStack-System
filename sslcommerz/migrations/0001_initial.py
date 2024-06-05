# Generated by Django 4.0.6 on 2022-09-06 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_number', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('val_transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('currency_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('consulation_fee', models.CharField(blank=True, max_length=255, null=True)),
                ('report_fee', models.CharField(blank=True, max_length=255, null=True)),
                ('card_type', models.CharField(blank=True, max_length=255, null=True)),
                ('card_no', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_date', models.CharField(blank=True, max_length=255, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('card_issuer', models.CharField(blank=True, max_length=255, null=True)),
                ('card_brand', models.CharField(blank=True, max_length=255, null=True)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.appointment')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
    ]
