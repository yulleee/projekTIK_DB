# Generated by Django 4.1.1 on 2022-10-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tendik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=20)),
                ('nip', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=100)),
                ('jabatan', models.CharField(max_length=100)),
            ],
        ),
    ]
