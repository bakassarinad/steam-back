# Generated by Django 3.0.4 on 2020-04-24 13:02

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200424_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('text', models.TextField()),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=api.models.Category, to='api.Game')),
            ],
        ),
    ]
