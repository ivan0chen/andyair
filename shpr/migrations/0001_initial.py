# Generated by Django 2.1 on 2018-09-28 08:45

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
            name='Shpr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('cscode', models.CharField(max_length=7, unique=True)),
                ('kind', models.CharField(blank=True, max_length=1)),
                ('csname', models.CharField(blank=True, max_length=60)),
                ('address', models.CharField(blank=True, max_length=120)),
                ('tel1', models.CharField(blank=True, max_length=20)),
                ('tel2', models.CharField(blank=True, max_length=20)),
                ('fax1', models.CharField(blank=True, max_length=20)),
                ('fax2', models.CharField(blank=True, max_length=20)),
                ('tlx', models.CharField(blank=True, max_length=20)),
                ('attn', models.CharField(blank=True, max_length=30)),
                ('dest', models.CharField(blank=True, max_length=3)),
                ('shipno', models.CharField(blank=True, max_length=7)),
                ('remark', models.CharField(blank=True, max_length=60)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shpr_shpr_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(blank=True, db_column='last_updated_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shpr_shpr_last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
