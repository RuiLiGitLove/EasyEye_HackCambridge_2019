# Generated by Django 2.1.3 on 2019-01-19 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecondData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('blink', models.PositiveSmallIntegerField(default=0)),
                ('direction', models.PositiveSmallIntegerField(default=0)),
                ('squint', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]