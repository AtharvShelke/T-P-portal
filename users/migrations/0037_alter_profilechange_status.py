# Generated by Django 4.2.5 on 2024-05-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_remove_profilechange_responded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilechange',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
