# Generated by Django 4.2.7 on 2023-12-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0010_csvsubject_question_question_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="choice_code",
            field=models.IntegerField(default=0),
        ),
    ]
