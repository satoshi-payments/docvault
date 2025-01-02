# Generated by Django 3.2.12 on 2022-03-11 16:21

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("paperless_mail", "0011_remove_mailrule_assign_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailrule",
            name="assign_tags",
            field=models.ManyToManyField(
                blank=True,
                to="documents.Tag",
                verbose_name="assign this tag",
            ),
        ),
    ]
