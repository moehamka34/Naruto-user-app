# Generated by Django 4.0.6 on 2022-07-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_ninja_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninja',
            name='jitsus',
            field=models.ManyToManyField(to='main_app.jitsu'),
        ),
    ]
