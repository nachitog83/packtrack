# Generated by Django 3.0.5 on 2020-06-05 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20200605_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='origin',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='origin',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='origin',
            name='house_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='origin',
            name='latitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='origin',
            name='longitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='origin',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='origin',
            name='province',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='origin',
            name='street',
            field=models.CharField(max_length=50),
        ),
    ]
