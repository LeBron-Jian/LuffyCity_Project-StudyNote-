# Generated by Django 2.2.6 on 2019-12-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authDemo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, 'VIP'), (2, 'SVIP'), (3, 'Oridinary')], default=3),
        ),
    ]
