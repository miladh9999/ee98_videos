# Generated by Django 3.1 on 2020-09-20 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20200921_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='topic',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
