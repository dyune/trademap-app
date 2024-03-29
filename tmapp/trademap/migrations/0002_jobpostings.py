# Generated by Django 5.0.1 on 2024-01-28 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trademap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPostings',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trademap.account')),
                ('user', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=40)),
                ('cost_offer', models.IntegerField()),
                ('profession_type', models.CharField(max_length=40)),
            ],
            bases=('trademap.account',),
        ),
    ]
