# Generated by Django 4.2.4 on 2023-08-27 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0012_alter_employé_id_congés_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employé',
            name='Id_Banque',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.banque'),
        ),
        migrations.AlterField(
            model_name='employé',
            name='Id_CNSS',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.cnss'),
        ),
        migrations.AlterField(
            model_name='employé',
            name='Id_Congés',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.congés'),
        ),
    ]
