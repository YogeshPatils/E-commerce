# Generated by Django 5.1.7 on 2025-03-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_customusermodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
