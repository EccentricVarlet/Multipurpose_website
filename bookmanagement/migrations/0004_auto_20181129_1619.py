# Generated by Django 2.1.2 on 2018-11-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanagement', '0003_auto_20181129_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktransactionmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Not Refund', 'Not Refund'), ('Refund', 'Refund')], default='Pending', max_length=32),
        ),
    ]
