# Generated by Django 5.1.1 on 2024-09-07 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorAccountPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('view', 'View Only'), ('full', 'Full Access'), ('transaction', 'Transaction Only')], max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.investmentaccount')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.investor')),
            ],
        ),
        migrations.AddField(
            model_name='investmentaccount',
            name='investors',
            field=models.ManyToManyField(through='investment.InvestorAccountPermission', to='investment.investor'),
        ),
    ]
