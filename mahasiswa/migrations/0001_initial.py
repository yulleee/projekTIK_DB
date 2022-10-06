# Generated by Django 4.1.1 on 2022-10-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttl', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('nim', models.IntegerField()),
                ('nama', models.CharField(max_length=200)),
                ('fakultas', models.CharField(max_length=100)),
                ('prodi', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]