# Generated by Django 4.0 on 2023-03-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_graphic_remove_sites_graphics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defaultpic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
