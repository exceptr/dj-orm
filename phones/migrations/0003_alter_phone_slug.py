# Generated by Django 4.0.6 on 2022-07-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_image_alter_phone_lte_exists_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(),
        ),
    ]
