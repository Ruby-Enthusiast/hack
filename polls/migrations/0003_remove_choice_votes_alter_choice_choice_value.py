# Generated by Django 4.2.7 on 2023-12-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_choice"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="choice",
            name="votes",
        ),
        migrations.AlterField(
            model_name="choice",
            name="choice_value",
            field=models.IntegerField(
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")], default=1
            ),
        ),
    ]