# Generated by Django 2.1 on 2018-09-18 14:50

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
            name='Custcsn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('cuno', models.CharField(max_length=10, unique=True)),
                ('cucd', models.CharField(blank=True, max_length=1)),
                ('cunme', models.CharField(blank=True, max_length=40)),
                ('cuid', models.CharField(blank=True, max_length=8)),
                ('cunmc', models.CharField(blank=True, max_length=40)),
                ('cuchadd1', models.CharField(blank=True, max_length=30)),
                ('cuchadd2', models.CharField(blank=True, max_length=30)),
                ('cuenadd1', models.CharField(blank=True, max_length=30)),
                ('cuenadd2', models.CharField(blank=True, max_length=30)),
                ('cuenadd3', models.CharField(blank=True, max_length=30)),
                ('cudir', models.CharField(blank=True, max_length=20)),
                ('cutel', models.CharField(blank=True, max_length=20)),
                ('cufax', models.CharField(blank=True, max_length=20)),
                ('cupcfax', models.CharField(blank=True, max_length=20)),
                ('cuattn', models.CharField(blank=True, max_length=30)),
                ('cunminv', models.CharField(blank=True, max_length=40)),
                ('cusale', models.CharField(blank=True, max_length=8)),
                ('custmk', models.CharField(blank=True, max_length=40)),
                ('cucgdt', models.DateTimeField(blank=True)),
                ('cucrdt', models.DateTimeField(blank=True)),
                ('cutrdt', models.DateTimeField(blank=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custcsn_custcsn_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(blank=True, db_column='last_updated_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custcsn_custcsn_last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
