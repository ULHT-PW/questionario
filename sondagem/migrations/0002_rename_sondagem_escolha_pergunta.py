# Generated by Django 4.1 on 2022-08-10 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sondagem", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="escolha",
            old_name="sondagem",
            new_name="pergunta",
        ),
    ]
