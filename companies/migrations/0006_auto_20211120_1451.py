# Generated by Django 3.2.9 on 2021-11-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_auto_20211114_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='company_id',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='companies/logo/default.png', null=True, upload_to='companies/logo/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo_min',
            field=models.ImageField(blank=True, default='companies/logo_min/default.png', null=True, upload_to='companies/logo_min/'),
        ),
        migrations.AlterField(
            model_name='guarantee',
            name='image',
            field=models.ImageField(blank=True, default='guarantees/default.png', null=True, upload_to='guarantees/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='companies/products/default.png', null=True, upload_to='companies/products/'),
        ),
    ]