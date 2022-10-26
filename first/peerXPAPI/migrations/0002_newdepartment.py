# Generated by Django 4.1.2 on 2022-10-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerXPAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, null=True, unique=True)),
                ('Description', models.TextField(max_length=250)),
                ('Created_by', models.BooleanField(blank=True, default=True, null=True)),
                ('Created_at', models.BooleanField()),
                ('Last_Updated_at', models.BooleanField()),
            ],
        ),
    ]
