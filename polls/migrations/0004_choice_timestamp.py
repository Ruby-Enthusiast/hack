# Generated by Django 4.2.7 on 2023-12-01 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0003_remove_choice_votes_alter_choice_choice_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
