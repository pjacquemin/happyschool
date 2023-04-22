# Generated by Django 2.2.4 on 2019-08-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
        ("student_absence_teacher", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentabsenceteachersettingsmodel",
            name="can_see_list",
            field=models.ManyToManyField(
                blank=True, default=None, related_name="can_see_list", to="auth.Group"
            ),
        ),
    ]
