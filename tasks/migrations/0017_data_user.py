# Generated by Django 4.1 on 2023-04-04 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0016_vacation_account_request_fecha_solicitada1_hasta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=25, null=True)),
                ('a_paterno', models.CharField(blank=True, max_length=15, null=True)),
                ('a_materno', models.CharField(blank=True, max_length=15, null=True)),
                ('reparticion', models.CharField(blank=True, max_length=10, null=True)),
                ('item', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
