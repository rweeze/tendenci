# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
    ]