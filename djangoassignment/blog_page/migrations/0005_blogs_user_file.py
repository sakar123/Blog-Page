# Generated by Django 3.0.8 on 2020-07-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_page', '0004_remove_blogs_user_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='user_file',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
