# Generated by Django 3.2.9 on 2021-11-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TakeOutSystem', '0005_alter_turnover_turn_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]