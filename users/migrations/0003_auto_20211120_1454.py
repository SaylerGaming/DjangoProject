# Generated by Django 3.2.9 on 2021-11-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211120_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
