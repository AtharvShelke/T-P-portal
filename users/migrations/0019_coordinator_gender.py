# Generated by Django 4.2.5 on 2024-03-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_rename_drive_id_driveapplication_drive_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinator',
            name='GENDER',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True),
        ),
    ]
