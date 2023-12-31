# Generated by Django 4.2.4 on 2023-08-26 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0011_congés_employé_id_congés'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employé',
            name='Id_Congés',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.congés', unique=True),
        ),
        migrations.AlterField(
            model_name='employé',
            name='Salaire_de_Base',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8),
        ),
    ]
