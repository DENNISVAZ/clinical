# Generated by Django 3.1.4 on 2020-12-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preconsults', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preconsult',
            name='checklink',
            field=models.BooleanField(default=False),
        ),
    ]
