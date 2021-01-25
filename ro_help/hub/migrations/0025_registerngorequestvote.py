# Generated by Django 3.0.4 on 2020-03-21 15:13

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0024_auto_20200322_1645"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegisterNGORequestVote",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified"),
                ),
                ("entity", models.CharField(max_length=30)),
                (
                    "vote",
                    models.CharField(
                        choices=[("YES", "YES"), ("NO", "NO"), ("ABSTENTION", "ABSTENTION")],
                        default="ABSTENTION",
                        max_length=10,
                        verbose_name="Vote",
                    ),
                ),
                (
                    "motivation",
                    models.TextField(help_text="Motivate your decision", max_length=500, verbose_name="Motvation"),
                ),
                (
                    "ngo_request",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="hub.RegisterNGORequest"),
                ),
            ],
            options={
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
    ]
