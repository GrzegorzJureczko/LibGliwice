# Generated by Django 4.1.3 on 2023-01-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='pages',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
