# Generated by Django 4.0.1 on 2022-07-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serveradd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servertype', models.TextField(max_length=100)),
                ('servername', models.TextField(max_length=100)),
            ],
        ),
    ]
