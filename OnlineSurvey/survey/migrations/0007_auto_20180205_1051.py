# Generated by Django 2.0.1 on 2018-02-05 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20180205_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveydesingform',
            old_name='label',
            new_name='lebel_data',
        ),
    ]
