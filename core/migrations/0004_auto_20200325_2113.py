# Generated by Django 3.0.2 on 2020-03-26 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_auto_20200325_2108'),
        ('avaliacoes', '0001_initial'),
        ('core', '0003_pontoturistico_atracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacao',
            field=models.ManyToManyField(to='avaliacoes.Avaliacoes'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='comentario',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]