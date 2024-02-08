# Generated by Django 5.0.1 on 2024-02-05 04:58

import django_summernote.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240128_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
