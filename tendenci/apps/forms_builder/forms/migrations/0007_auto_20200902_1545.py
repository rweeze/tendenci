# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20200206_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='form',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
    ]
