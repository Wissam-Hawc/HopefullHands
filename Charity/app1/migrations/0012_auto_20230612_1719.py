# Generated by Django 3.1.7 on 2023-06-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20230612_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='program_challenge',
            field=models.CharField(default='Default Value', max_length=2000),
        ),
        migrations.AddField(
            model_name='program',
            name='program_objective',
            field=models.CharField(default='Default Value', max_length=2000),
        ),
    ]
