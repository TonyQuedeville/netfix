# Generated by Django 3.2.12 on 2023-09-13 19:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_companyreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyreview',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyreview',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
