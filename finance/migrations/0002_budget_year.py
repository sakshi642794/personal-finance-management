# Generated by Django 4.2.23 on 2025-07-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="budget",
            name="year",
            field=models.IntegerField(default=2025),
            preserve_default=False,
        ),
    ]
