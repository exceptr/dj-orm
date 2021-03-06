# Generated by Django 4.0.6 on 2022-07-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=100)),
                ('release_date', models.DateField(max_length=30)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]
