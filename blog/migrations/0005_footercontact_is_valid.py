# Generated by Django 3.1.3 on 2020-11-24 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_footercontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='footercontact',
            name='is_valid',
            field=models.BooleanField(default=True, unique=True),
            preserve_default=False,
        ),
    ]
