# Generated by Django 2.2.13 on 2020-12-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_auto_20200831_2006"),
    ]

    operations = [
        migrations.AlterField(
            model_name="givencoursemodel",
            name="group",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
    ]
