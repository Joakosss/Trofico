# Generated by Django 5.1 on 2024-08-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0004_alter_planta_descripcion_r_ambiente'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='relativa',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='temperatura',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]