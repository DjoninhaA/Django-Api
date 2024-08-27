# Generated by Django 5.1 on 2024-08-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_age', models.IntegerField(default=0)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
