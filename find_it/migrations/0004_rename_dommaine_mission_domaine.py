# Generated by Django 3.2.4 on 2021-08-10 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find_it', '0003_entrepriseparticulier_domaine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='dommaine',
            new_name='domaine',
        ),
    ]
