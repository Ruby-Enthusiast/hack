# Generated by Django 4.2.7 on 2023-12-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="code",
            field=models.CharField(default=101, max_length=10),
            preserve_default=False,
        ),
    ]
