# Generated by Django 5.1.7 on 2025-03-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_customusermodel_otp_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
