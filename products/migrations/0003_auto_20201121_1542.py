# Generated by Django 3.1.1 on 2020-11-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201121_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deals',
            field=models.IntegerField(choices=[(0, 0), (5, 5), (10, 10), (15, 15), (20, 20), (25, 25), (30, 30), (35, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90), (95, 95)], null=True),
        ),
    ]