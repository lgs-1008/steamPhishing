# Generated by Django 2.2.7 on 2020-01-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.CharField(max_length=30)),
                ('UserPassword', models.CharField(max_length=30)),
            ],
        ),
    ]
