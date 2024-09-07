# Generated by Django 5.1.1 on 2024-09-07 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0002_investmentaccount_investoraccountpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.investmentaccount')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.investor')),
            ],
        ),
    ]
