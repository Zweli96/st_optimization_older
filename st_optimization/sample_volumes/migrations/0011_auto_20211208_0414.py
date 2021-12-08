# Generated by Django 3.2.8 on 2021-12-08 02:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sample_volumes', '0010_auto_20211127_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_type', models.CharField(max_length=200, null=True)),
                ('sample_type_long', models.CharField(max_length=200, null=True)),
                ('sample_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DELETED', 'DELETED')], max_length=200, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sample_volumes',
            name='reported_by',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sample_volumes',
            name='reported_date',
            field=models.DateTimeField(default=datetime.date.today, null=True),
        ),
        migrations.DeleteModel(
            name='Sample_Types',
        ),
        migrations.AlterField(
            model_name='sample_volumes',
            name='sample_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample_volumes.sampletype'),
        ),
    ]