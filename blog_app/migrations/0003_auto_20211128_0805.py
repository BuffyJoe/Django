# Generated by Django 3.2.7 on 2021-11-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Topic',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='topic',
        ),
    ]
