# Generated by Django 5.1.6 on 2025-02-12 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('Segunda', 'Segunda-feira'), ('Terça', 'Terça-feira'), ('Quarta', 'Quarta-feira'), ('Quinta', 'Quinta-feira'), ('Sexta', 'Sexta-feira'), ('Sábado', 'Sábado')], max_length=10)),
                ('horario', models.TimeField()),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turmas.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('turma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='turmas.turma')),
            ],
        ),
    ]
