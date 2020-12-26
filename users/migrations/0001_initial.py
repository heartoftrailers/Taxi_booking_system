# Generated by Django 3.1.3 on 2020-12-23 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_color', models.CharField(max_length=50)),
                ('car_license_plate', models.CharField(max_length=50)),
            ],
        ),
    ]
