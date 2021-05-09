# Generated by Django 3.2.2 on 2021-05-09 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cases', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('recovered', models.IntegerField()),
                ('countryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.country')),
            ],
        ),
    ]
