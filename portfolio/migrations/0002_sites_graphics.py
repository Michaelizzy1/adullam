# Generated by Django 4.0 on 2023-03-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='graphics',
            field=models.ImageField(default='text', upload_to=''),
            preserve_default=False,
        ),
    ]
