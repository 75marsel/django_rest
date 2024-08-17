# Generated by Django 5.1 on 2024-08-17 13:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("card_title", models.CharField(max_length=100)),
                ("card_text", models.TextField(max_length=200)),
                ("card_email", models.EmailField(max_length=100)),
                ("card_link", models.URLField()),
                ("card_footer", models.CharField(max_length=100)),
                ("card_username", models.CharField(max_length=20)),
            ],
        ),
    ]