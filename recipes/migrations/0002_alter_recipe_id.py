# Generated by Django 4.2.9 on 2024-01-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.FloatField(primary_key=True, serialize=False),
        ),
    ]
