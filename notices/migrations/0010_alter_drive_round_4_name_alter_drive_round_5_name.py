# Generated by Django 4.2.5 on 2024-04-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0009_drive_num_rounds_drive_round_1_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='round_4_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Round 4 Name'),
        ),
        migrations.AlterField(
            model_name='drive',
            name='round_5_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Round 5 Name'),
        ),
    ]
