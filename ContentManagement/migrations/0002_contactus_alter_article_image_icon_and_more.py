# Generated by Django 4.1.7 on 2023-03-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContentManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='image_icon',
            field=models.ImageField(blank=True, null=True, upload_to='static/articleicon/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='main_home_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/articlehome/'),
        ),
    ]
