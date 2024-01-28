# Generated by Django 5.0.1 on 2024-01-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trademap', '0002_jobpostings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostings',
            name='profession_type',
            field=models.CharField(choices=[('Plumber', 'Plumber'), ('Carpenter', 'Carpenter'), ('Electrician', 'Electrician'), ('Landscaper', 'Landscaper'), ('Painter or Decorator', 'Painter or Decorator'), ('Other', 'Other')], max_length=40),
        ),
    ]
