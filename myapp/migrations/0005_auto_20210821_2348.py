# Generated by Django 3.2 on 2021-08-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_graph_mygraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mygraph',
            name='dt',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='mygraph',
            name='interval',
            field=models.PositiveIntegerField(),
        ),
    ]
