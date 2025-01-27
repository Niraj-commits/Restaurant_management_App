# Generated by Django 5.1.5 on 2025-01-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_mgmt_system', '0003_rename_number_table_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('p', 'pending'), ('a', 'accepted')], default='p', max_length=25),
        ),
    ]
