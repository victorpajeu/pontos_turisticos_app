# Generated by Django 3.0.2 on 2020-03-25 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0002_auto_20200325_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracao',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
