# Generated by Django 4.2.6 on 2023-12-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='jogador',
        ),
        migrations.AddField(
            model_name='partida',
            name='local',
            field=models.CharField(default='IFRN - campus Natal-Central', help_text='Local da partida.', max_length=200),
        ),
    ]
