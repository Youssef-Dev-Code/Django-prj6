# Generated by Django 4.2.4 on 2023-08-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0006_alter_cnss_numero_alter_employé_cin'),
    ]

    operations = [
        migrations.AddField(
            model_name='employé',
            name='Matricule',
            field=models.BigIntegerField(default=1010),
            preserve_default=False,
        ),
    ]
