# Generated by Django 3.2.8 on 2021-12-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_volumes', '0014_alter_sample_volumes_reported_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample_volumes',
            name='reported_date',
            field=models.DateTimeField(null=True),
        ),
    ]
