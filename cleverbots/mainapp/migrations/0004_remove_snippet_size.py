# Generated by Django 2.1.3 on 2019-04-17 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190417_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='size',
        ),
    ]