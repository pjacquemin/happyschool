# Generated by Django 2.2.13 on 2021-02-02 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pia', '0021_auto_20210202_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branchgoalmodel',
            options={'ordering': ['-date_end', '-date_start']},
        ),
        migrations.AlterModelOptions(
            name='crossgoalmodel',
            options={'ordering': ['-date_end', '-date_start']},
        ),
    ]
