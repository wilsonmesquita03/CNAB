# Generated by Django 4.1.5 on 2023-01-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnab', '0002_alter_cnab_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnab',
            name='value',
            field=models.FloatField(),
        ),
    ]
