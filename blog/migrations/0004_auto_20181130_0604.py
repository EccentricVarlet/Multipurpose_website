# Generated by Django 2.1.2 on 2018-11-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181129_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, default='book1.jpeg', null=True, upload_to='%Y/%m/%d'),
        ),
    ]
