# Generated by Django 4.0.1 on 2022-02-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
