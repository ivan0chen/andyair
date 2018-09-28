# Generated by Django 2.1 on 2018-09-28 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custcsn', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cneecrd',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('custcsn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='cneecrd_custcsn', serialize=False, to='custcsn.Custcsn')),
                ('crdamt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('aro', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ars', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('arc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('arcod', models.IntegerField(blank=True, default=0, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cneecrd_cneecrd_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(blank=True, db_column='last_updated_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cneecrd_cneecrd_last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
