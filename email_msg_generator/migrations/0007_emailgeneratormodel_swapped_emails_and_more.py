# Generated by Django 4.2.2 on 2023-06-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("email_msg_generator", "0006_emailgeneratormodel_delete_emailgenerator"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailgeneratormodel",
            name="swapped_emails",
            field=models.FileField(null=True, upload_to="swapped"),
        ),
        migrations.AlterField(
            model_name="emailgeneratormodel",
            name="generated_emails",
            field=models.FileField(null=True, upload_to="messages"),
        ),
    ]