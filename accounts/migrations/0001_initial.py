# Generated by Django 2.2 on 2020-01-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=30, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Your Email Address')),
                ('full_name', models.CharField(blank=True, max_length=30, verbose_name='Full Name')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]