# Generated by Django 4.1.7 on 2023-03-22 09:06

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('art_title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('release_date', models.DateTimeField()),
                ('main_home_image', models.ImageField(blank=True, null=True, upload_to='articlehome/')),
                ('image_icon', models.ImageField(blank=True, null=True, upload_to='articleicon/')),
                ('release_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContentManagement.section')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
