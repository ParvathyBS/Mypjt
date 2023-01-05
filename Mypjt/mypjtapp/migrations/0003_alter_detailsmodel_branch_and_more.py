# Generated by Django 4.1.1 on 2023-01-05 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypjtapp', '0002_alter_detailsmodel_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsmodel',
            name='Branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mypjtapp.branchmodel'),
        ),
        migrations.AlterField(
            model_name='detailsmodel',
            name='District',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mypjtapp.districtmodel'),
        ),
    ]