# Generated by Django 3.0.8 on 2020-07-24 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_page', '0002_auto_20200721_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='user_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]