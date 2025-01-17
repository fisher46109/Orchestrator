# Generated by Django 5.0.6 on 2024-06-26 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestrator_app', '0007_alter_process_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='machine_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='result',
            field=models.CharField(blank=True, default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='process',
            name='robot_update_flag',
            field=models.CharField(blank=True, default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='process',
            name='ssk_flag',
            field=models.CharField(blank=True, default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='process',
            name='state',
            field=models.CharField(blank=True, default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='process',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orchestrator_app.user'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='robot_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='process',
            unique_together={('machine', 'user')},
        ),
    ]
