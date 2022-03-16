# Generated by Django 3.1.1 on 2020-11-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20201026_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='external_link',
            field=models.CharField(default='', help_text='Add a external link or contact of website.', max_length=500),
            preserve_default=False,
        ),
    ]
