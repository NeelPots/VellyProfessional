# Generated by Django 4.2.1 on 2023-07-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Footer",
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
                ("name", models.CharField(max_length=122)),
                ("email", models.CharField(max_length=122)),
                ("message", models.TextField()),
                ("date", models.DateField()),
            ],
        ),
    ]
