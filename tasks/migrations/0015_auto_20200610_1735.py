# Generated by Django 3.0.5 on 2020-06-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_auto_20200610_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='origin',
            name='pos_code',
            field=models.IntegerField(blank=True),
        ),
    ]
