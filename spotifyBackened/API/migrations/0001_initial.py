# Generated by Django 4.2.2 on 2023-06-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
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
                (
                    "room_code",
                    models.CharField(default=None, max_length=10, unique=True),
                ),
                ("host_name", models.CharField(max_length=20, unique=True)),
                ("guest_can_stop", models.BooleanField(default=False)),
                ("votes_to_change", models.IntegerField(default=1)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
