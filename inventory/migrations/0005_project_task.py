# Generated by Django 4.1.7 on 2023-03-23 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.task'),
            preserve_default=False,
        ),
    ]
