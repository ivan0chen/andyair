# Generated by Django 2.1 on 2018-09-29 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exrate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=3, unique=True)),
                ('currency', models.CharField(blank=True, max_length=25)),
                ('ex_irate', models.DecimalField(blank=True, decimal_places=5, max_digits=9, null=True)),
                ('ex_orate', models.DecimalField(blank=True, decimal_places=5, max_digits=9, null=True)),
                ('lastdate', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exrate_exrate_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(blank=True, db_column='last_updated_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exrate_exrate_last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
