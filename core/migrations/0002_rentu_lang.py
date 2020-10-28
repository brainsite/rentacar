# Generated by Django 2.2.16 on 2020-10-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentu',
            name='lang',
            field=models.CharField(blank=True, choices=[('RU', 'Русский'), ('EN', 'English')], default='RU', max_length=20, null=True, verbose_name='Язык пользователя.'),
        ),
    ]