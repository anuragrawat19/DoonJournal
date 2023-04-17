# Generated by Django 4.1.7 on 2023-04-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(default='kedar', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='main_home_image',
            field=models.ImageField(blank=True, help_text='Please Upload the image size of 756 * 411', null=True, upload_to='places/'),
        ),
    ]