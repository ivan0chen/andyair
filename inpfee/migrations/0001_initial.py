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
            name='Inpfee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=3, unique=True)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('tax', models.CharField(blank=True, max_length=1)),
                ('ocamt', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inpfee_inpfee_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(blank=True, db_column='last_updated_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inpfee_inpfee_last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
