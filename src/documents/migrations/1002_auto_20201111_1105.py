# Generated by Django 3.1.3 on 2020-11-11 11:05

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1001_auto_20201109_1636"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="filename",
            field=models.FilePathField(
                default=None,
                editable=False,
                help_text="Current filename in storage",
                max_length=1024,
                null=True,
            ),
        ),
    ]
