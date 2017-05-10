# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-09 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_payroll_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payroll',
            old_name='employee_id',
            new_name='employee',
        ),
        migrations.AddField(
            model_name='payroll',
            name='amount_before_deductions',
            field=models.DecimalField(blank=True, decimal_places=2, default=15000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payroll',
            name='date_generated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payroll',
            name='date_paid',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payroll',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]