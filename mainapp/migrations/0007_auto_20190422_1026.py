# Generated by Django 2.1.4 on 2019-04-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20190418_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='size',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]