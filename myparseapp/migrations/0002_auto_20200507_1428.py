# Generated by Django 3.0.5 on 2020-05-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myparseapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresume',
            name='exp',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='fname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='lname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='phno',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='pin',
            field=models.CharField(max_length=10),
        ),
    ]