# Generated by Django 2.2.8 on 2020-03-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pia', '0012_auto_20200312_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='piasettingsmodel',
            name='filter_teacher_entries_by_tenure',
            field=models.BooleanField(default=True, help_text='\n        Si activé, seuls les titulaires peuvent voir les PIA de leurs élèves.\n        Sinon sera limité aux classes associées.\n        '),
        ),
    ]
