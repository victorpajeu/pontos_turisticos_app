# Generated by Django 3.0.2 on 2020-03-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('descrição', models.TextField(verbose_name='descrição')),
                ('aprovado', models.BooleanField(verbose_name='status')),
            ],
        ),
    ]