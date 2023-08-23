# Generated by Django 4.2.4 on 2023-08-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0008_employé_télephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banque',
            name='Paiement',
            field=models.CharField(choices=[('Chèque', 'Chèque'), ('Virement', 'Virement'), ('Espèce', 'Espèce')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='etat_contrat',
            name='Designation',
            field=models.CharField(choices=[('SVIP', 'SIVP'), ('Contractuel', 'Contractuel'), ('Occasionnel', 'Occasionnel'), ('Permanent', 'Permanent'), ('Titulaire', 'Titulaire')], max_length=20),
        ),
        migrations.AlterField(
            model_name='local',
            name='Designation',
            field=models.CharField(choices=[('Siège', 'Siège'), ('Marsa corniche', 'Marsa corniche'), ('MMarsa saada', 'Marsa saada'), ('Tunis city', 'Tunis city'), ('Azur city', 'Azur city'), ('Mall of Sousse', 'Mall of Sousse'), ('Mall de Tunis', 'Mall de Tunis')], max_length=25),
        ),
        migrations.AlterField(
            model_name='situation',
            name='Sexe',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=10),
        ),
        migrations.AlterField(
            model_name='situation',
            name='sit_conjug',
            field=models.CharField(choices=[('Marié', 'Marié'), ('Célibataire', 'Célibataire'), ('Divorcé', 'Divorcé'), ('Veufe', 'Veufe')], max_length=40),
        ),
    ]