# Generated by Django 3.0.7 on 2020-07-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('off', models.IntegerField()),
                ('price', models.IntegerField()),
                ('field', models.CharField(max_length=100)),
                ('sub1', models.CharField(max_length=100)),
                ('sub2', models.CharField(max_length=100)),
                ('sub3', models.CharField(max_length=100)),
                ('sub4', models.CharField(max_length=100)),
                ('sub5', models.CharField(max_length=100)),
            ],
        ),
    ]
