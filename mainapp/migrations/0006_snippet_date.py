# Generated by Django 2.1.4 on 2019-04-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_snippet_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
