# Generated by Django 5.1.3 on 2024-12-15 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='summary',
            field=models.CharField(default='yet to be summarized', max_length=200),
            preserve_default=False,
        ),
    ]
