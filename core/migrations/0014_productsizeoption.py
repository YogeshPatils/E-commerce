# Generated by Django 5.1.7 on 2025-03-18 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_productvarient_extra_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSizeOption',
            fields=[
                ('size_id', models.AutoField(primary_key=True, serialize=False)),
                ('size_category', models.CharField(max_length=100)),
                ('size_name', models.CharField(max_length=100)),
                ('stock_in_qty', models.IntegerField()),
                ('product_varient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productvarient')),
            ],
        ),
    ]
