# Generated by Django 3.1.3 on 2020-11-21 21:51

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("paperless_mail", "0003_auto_20201118_1940"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailrule",
            name="order",
            field=models.IntegerField(default=0),
        ),
    ]