# Generated by Django 4.0 on 2022-03-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('describtion', models.TextField()),
                ('logo', models.ImageField(upload_to='logo/')),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=200)),
                ('youtube', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
