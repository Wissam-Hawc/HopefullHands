# Generated by Django 4.2.2 on 2023-06-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_program_program_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='status',
            field=models.CharField(default='success', max_length=50),
        ),
    ]
