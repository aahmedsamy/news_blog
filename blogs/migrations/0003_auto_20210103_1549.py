# Generated by Django 3.1.4 on 2021-01-03 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_category_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]