# Generated by Django 4.2.1 on 2023-05-15 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobooks',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
