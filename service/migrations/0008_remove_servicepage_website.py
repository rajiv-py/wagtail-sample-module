# Generated by Django 3.1.1 on 2020-11-24 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20201124_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicepage',
            name='website',
        ),
    ]
