# Generated by Django 3.0.4 on 2020-03-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200326_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(null=True, verbose_name='aprovado'),
        ),
    ]
