# Generated by Django 4.2.5 on 2024-04-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0008_drive_resume_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='num_rounds',
            field=models.IntegerField(default=1, verbose_name='Number of Rounds'),
        ),
        migrations.AddField(
            model_name='drive',
            name='round_1_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Round 1 Name'),
        ),
        migrations.AddField(
            model_name='drive',
            name='round_2_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Round 2 Name'),
        ),
        migrations.AddField(
            model_name='drive',
            name='round_3_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Round 3 Name'),
        ),
        migrations.AddField(
            model_name='drive',
            name='round_4_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Round 3 Name'),
        ),
        migrations.AddField(
            model_name='drive',
            name='round_5_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Round 3 Name'),
        ),
    ]
