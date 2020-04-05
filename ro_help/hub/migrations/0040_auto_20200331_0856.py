# Generated by Django 3.0.4 on 2020-03-31 08:56

from django.db import migrations, models
import hub.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0039_auto_20200330_2151"),
    ]

    operations = [
        migrations.AlterField(

            model_name="registerngorequest",
            name="last_balance_sheet",
            field=models.FileField(
                max_length=300,
                storage=hub.storage_backends.PrivateMediaStorage(),
                upload_to="",
                verbose_name="First page of last balance sheet",
            ),
        ),
        migrations.AlterField(
            model_name="registerngorequest",
            name="statute",
            field=models.FileField(
                max_length=300,
                storage=hub.storage_backends.PrivateMediaStorage(),
                upload_to="",
                verbose_name="NGO Statute",
            ),
        ),
    ]
