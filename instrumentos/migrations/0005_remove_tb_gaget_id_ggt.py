# Generated by Django 2.0.2 on 2018-05-03 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentos', '0004_tb_gaget_id_ggt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_gaget',
            name='id_ggt',
        ),
    ]
