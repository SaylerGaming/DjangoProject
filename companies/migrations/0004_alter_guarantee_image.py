# Generated by Django 3.2.9 on 2021-11-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20211113_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guarantee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]