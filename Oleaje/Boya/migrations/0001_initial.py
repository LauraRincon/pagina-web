# Generated by Django 2.0.7 on 2018-07-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('Hs', models.IntegerField()),
                ('Tm02', models.IntegerField()),
                ('Tp', models.IntegerField()),
                ('Tz', models.IntegerField()),
                ('Hm0', models.IntegerField()),
                ('Hmax', models.IntegerField()),
                ('H1_10', models.IntegerField()),
            ],
        ),
    ]
