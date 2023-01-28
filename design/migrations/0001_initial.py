# Generated by Django 4.1.5 on 2023-01-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyData",
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
                ("title", models.CharField(max_length=100)),
                ("details", models.TextField(max_length=2000)),
                ("done", models.BooleanField(default=False)),
                ("created_data", models.DateTimeField()),
            ],
        ),
    ]
