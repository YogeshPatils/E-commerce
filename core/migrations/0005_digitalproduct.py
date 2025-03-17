# Generated by Django 5.1.5 on 2025-03-17 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_order_user_id_remove_payment_order_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalProduct',
            fields=[
                ('digital_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_url', models.TextField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
    ]
