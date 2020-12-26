# Generated by Django 3.1.3 on 2020-12-23 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20201223_2244'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_time', models.DateTimeField()),
                ('pick_up_place', models.CharField(max_length=80)),
                ('drop_off_place', models.CharField(max_length=80)),
                ('payment_method', models.CharField(choices=[('1', 'Card'), ('2', 'Cash')], max_length=1)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.driver')),
            ],
        ),
    ]
