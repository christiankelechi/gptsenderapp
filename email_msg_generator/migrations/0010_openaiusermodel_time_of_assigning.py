# Generated by Django 4.2.2 on 2023-07-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("email_msg_generator", "0009_usercredentials"),
    ]

    operations = [
        migrations.AddField(
            model_name="openaiusermodel",
            name="time_of_assigning",
            field=models.DateTimeField(auto_now=True),
        ),
    ]