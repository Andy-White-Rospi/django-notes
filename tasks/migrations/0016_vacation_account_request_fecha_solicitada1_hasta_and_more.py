# Generated by Django 4.1 on 2023-04-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_vacation_account_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation_account_request',
            name='fecha_solicitada1_hasta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vacation_account_request',
            name='fecha_solicitada2_hasta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vacation_account_request',
            name='fecha_solicitada3_hasta',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
