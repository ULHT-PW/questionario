# Generated by Django 4.1 on 2022-08-10 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sessao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Pergunta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("texto_pergunta", models.CharField(max_length=200)),
                ("ativa", models.BooleanField(default=False)),
                (
                    "sessao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sondagem.sessao",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Escolha",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("votos", models.IntegerField(default=0)),
                ("texto_escolha", models.CharField(max_length=200)),
                (
                    "sondagem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sondagem.pergunta",
                    ),
                ),
            ],
        ),
    ]
