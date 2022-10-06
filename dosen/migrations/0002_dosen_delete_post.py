# Generated by Django 4.1.1 on 2022-10-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=50)),
                ('nip', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]