# Generated by Django 4.2.5 on 2024-03-12 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='Reference_no',
            field=models.CharField(default='hehe', max_length=100),
        ),
        migrations.AddField(
            model_name='drive',
            name='application_link',
            field=models.CharField(blank=True, default='hehe', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drive',
            name='shared_on_date',
            field=models.DateField(default='2001-02-12'),
        ),
    ]
