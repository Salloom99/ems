# Generated by Django 4.1a1 on 2022-07-22 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("asset", "0003_alter_employee_department"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="reporter",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assets",
                to="asset.employee",
            ),
            preserve_default=False,
        ),
    ]
