# Generated by Django 3.2.4 on 2021-08-09 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EntrepriseParticulier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=254)),
                ('logo', models.ImageField(null=True, upload_to='uploadslogo')),
                ('description', models.CharField(max_length=254)),
                ('adresse', models.CharField(max_length=254, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=254)),
                ('nom', models.CharField(max_length=254)),
                ('domaine', models.CharField(choices=[('1', 'developement web'), ('2', 'art grafique'), ('3', 'developement mobile'), ('4', 'cybersecuriter')], max_length=254, null=True)),
                ('competence', models.CharField(max_length=254)),
                ('sexe', models.CharField(max_length=254, null=True)),
                ('image', models.ImageField(null=True, upload_to='uploads')),
                ('date_naissance', models.DateField(null=True)),
                ('description', models.CharField(max_length=254, null=True)),
                ('adresse', models.CharField(max_length=254, null=True)),
                ('numero_telephone', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dommaine', models.CharField(choices=[('1', 'developement web'), ('2', 'art grafique'), ('3', 'developement mobile'), ('4', 'cybersecuriter')], max_length=254, null=True)),
                ('intituler', models.CharField(max_length=254, null=True)),
                ('date_debut', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateField(null=True)),
                ('description', models.CharField(max_length=254, null=True)),
                ('fourcette_prix', models.DecimalField(decimal_places=0, max_digits=8, null=True)),
                ('outils', models.TextField()),
                ('PE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='find_it.entrepriseparticulier')),
            ],
        ),
        migrations.CreateModel(
            name='Postuler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.TextField(null=True)),
                ('decription', models.TextField(null=True)),
                ('date_postula', models.DateTimeField()),
                ('itworker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='find_it.itworker')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='find_it.mission')),
            ],
        ),
    ]
