# Generated by Django 3.1.4 on 2021-01-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210103_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.FileField(default=1, upload_to='blogs/categories/icons'),
            preserve_default=False,
        ),
    ]