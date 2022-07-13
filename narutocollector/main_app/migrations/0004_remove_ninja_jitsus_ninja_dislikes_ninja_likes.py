# Generated by Django 4.0.6 on 2022-07-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_ninja_jitsus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninja',
            name='jitsus',
        ),
        migrations.AddField(
            model_name='ninja',
            name='dislikes',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ninja',
            name='likes',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]