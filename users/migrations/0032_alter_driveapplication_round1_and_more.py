# Generated by Django 4.2.5 on 2024-04-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_driveapplication_round1_driveapplication_round2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driveapplication',
            name='round1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driveapplication',
            name='round2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driveapplication',
            name='round3',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driveapplication',
            name='round4',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driveapplication',
            name='round5',
            field=models.BooleanField(default=False),
        ),
    ]
