# Generated by Django 4.1.2 on 2022-10-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerXPAPI', '0003_newtickect_manageticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtickect',
            name='Priority',
            field=models.PositiveSmallIntegerField(unique=True, verbose_name='priority'),
        ),
    ]
