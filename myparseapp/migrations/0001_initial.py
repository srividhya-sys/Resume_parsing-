# Generated by Django 3.0.5 on 2020-05-05 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentresume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('mail', models.EmailField(max_length=150)),
                ('phno', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('dist', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('pin', models.CharField(max_length=150)),
                ('education', models.CharField(max_length=150)),
                ('wstatus', models.CharField(max_length=150)),
                ('skill', models.CharField(max_length=150)),
                ('exp', models.CharField(max_length=150)),
            ],
        ),
    ]