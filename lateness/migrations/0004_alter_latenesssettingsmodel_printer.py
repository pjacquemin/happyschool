# Generated by Django 4.0.5 on 2023-01-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lateness', '0003_sanctiontriggermodel_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latenesssettingsmodel',
            name='printer',
            field=models.CharField(blank=True, help_text='IP address of one or multiple printers. If multiple, it must be separated by a comma ","', max_length=200),
        ),
    ]
