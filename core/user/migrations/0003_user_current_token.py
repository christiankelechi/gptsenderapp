# Generated by Django 4.2.2 on 2023-06-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core_user", "0002_user_open_ai_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="current_token",
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
