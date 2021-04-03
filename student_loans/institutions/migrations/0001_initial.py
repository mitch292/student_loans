# Generated by Django 3.1.7 on 2021-04-03 14:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('state', models.CharField(blank=True, max_length=4, null=True)),
                ('zip', models.CharField(blank=True, max_length=12, null=True)),
                ('type', models.CharField(choices=[('Public', 'Public'), ('Private Nonprofit', 'Private Nonprofit'), ('Proprietary', 'Proprietary'), ('Foreign For Profit', 'Foreign For Profit'), ('Foreign Private', 'Foreign Private'), ('Foreign Public', 'Foreign Public'), ('Unknown', 'Unkown')], max_length=255)),
                ('source_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
                ('quarter', models.CharField(blank=True, max_length=2, null=True)),
                ('loan_type', models.CharField(choices=[('Direct Loan Subsidized', 'Direct Subsidized'), ('Direct Loan Unsubsidized - Undergraduate', 'Direct Unsubsidized Undergraduate'), ('Direct Loan Unsubsidized - Graduate', 'Direct Unsubsidized Graduate'), ('Direct Loan Parent Plus', 'Direct Parent Plus'), ('Direct Loan Grad Plus', 'Direct Grad Plus')], max_length=255)),
                ('receipient_count', models.IntegerField(blank=True, null=True)),
                ('loans_originated_count', models.IntegerField()),
                ('loans_originated_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('disbursements_count', models.IntegerField(blank=True, null=True)),
                ('disbursements_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.institution')),
            ],
        ),
    ]
