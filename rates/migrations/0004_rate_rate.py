# Generated by Django 5.1.2 on 2024-10-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0003_remove_rate_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
