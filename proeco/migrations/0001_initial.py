# Generated by Django 2.2.8 on 2020-02-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OverwriteDataModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "people",
                    models.CharField(
                        choices=[("student", "Étudiant"), ("responsible", "Responsable")],
                        max_length=20,
                    ),
                ),
                (
                    "uid",
                    models.BigIntegerField(
                        help_text="Identifiant unique (matricule de l'étudiant ou du responsable)."
                    ),
                ),
                ("field", models.CharField(max_length=100)),
                ("value", models.CharField(max_length=100)),
            ],
        ),
    ]
