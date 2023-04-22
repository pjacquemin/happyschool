# Generated by Django 2.2.22 on 2021-06-14 12:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0014_menuentrymodel"),
        ("auth", "0011_update_proxy_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="SanctionTriggerModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("sanction_id", models.PositiveIntegerField(blank=True, null=True)),
                ("lateness_count_trigger_first", models.PositiveSmallIntegerField(default=4)),
                ("lateness_count_trigger", models.PositiveSmallIntegerField(default=3)),
                ("only_warn", models.BooleanField(default=False)),
                (
                    "next_week_day",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[
                            (None, "Choisir un jour de la semaine"),
                            (1, "Lundi"),
                            (2, "Mardi"),
                            (3, "Mercredi"),
                            (4, "Jeudi"),
                            (5, "Vendredi"),
                            (6, "Samedi"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "delay",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        default=1,
                        help_text="Le nombre de jour avant de postposer la sanction à la semaine d'après.\n        Par exemple, pour une valeur de 1, si le retard qui déclenche la sanction a lieu\n        le même jour de la semaine que la sanction, la sanction sera mise la semaine prochaine\n        parce qu'il y a moins de 1 jour de différence. Au contraire, si le retard à lieu 1 jour\n        avant le jour de sanction, la sanction sera mise le lendemain.",
                        null=True,
                    ),
                ),
                ("sanction_time", models.TimeField(blank=True, null=True)),
                (
                    "teaching",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.TeachingModel"
                    ),
                ),
                ("year", models.ManyToManyField(blank=True, to="core.YearModel")),
            ],
        ),
        migrations.CreateModel(
            name="LatenessSettingsModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("printer", models.CharField(blank=True, max_length=200)),
                ("date_count_start", models.DateField(default=datetime.date(2019, 9, 1))),
                ("notify_responsible", models.BooleanField(default=False)),
                ("enable_camera_scan", models.BooleanField(default=False)),
                ("all_access", models.ManyToManyField(blank=True, default=None, to="auth.Group")),
                ("teachings", models.ManyToManyField(default=None, to="core.TeachingModel")),
            ],
        ),
        migrations.CreateModel(
            name="LatenessModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("has_sanction", models.BooleanField(default=False)),
                ("sanction_id", models.PositiveIntegerField(blank=True, null=True)),
                ("justified", models.BooleanField(default=False)),
                (
                    "datetime_creation",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date et heure de création du retard"
                    ),
                ),
                (
                    "datetime_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Date et heure de mise à jour du retard"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.StudentModel",
                    ),
                ),
            ],
        ),
    ]
