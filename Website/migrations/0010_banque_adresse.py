# Generated by Django 4.2.4 on 2023-08-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0009_alter_banque_paiement_alter_etat_contrat_designation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banque',
            name='Adresse',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
