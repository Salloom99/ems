# Generated by Django 4.1a1 on 2022-05-30 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("asset", "0002_alter_asset_image_alter_department_admin_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="department",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="asset.department",
            ),
        ),
    ]
