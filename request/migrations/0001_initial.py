# Generated by Django 4.0.4 on 2022-05-28 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('approve_number', models.PositiveSmallIntegerField(default=0)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.asset')),
            ],
        ),
        migrations.CreateModel(
            name='FixRequest',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='request.request')),
                ('severity', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='L', max_length=255)),
                ('note', models.CharField(max_length=255)),
            ],
            bases=('request.request',),
        ),
        migrations.CreateModel(
            name='TransferRequest',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='request.request')),
                ('from_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='asset.department')),
                ('to_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='asset.department')),
            ],
            bases=('request.request',),
        ),
    ]
