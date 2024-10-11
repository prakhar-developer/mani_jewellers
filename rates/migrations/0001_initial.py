# Generated by Django 5.1.2 on 2024-10-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metal_type', models.CharField(max_length=10)),
                ('purity', models.CharField(max_length=10)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
