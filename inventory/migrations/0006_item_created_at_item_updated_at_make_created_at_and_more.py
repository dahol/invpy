# Generated by Django 4.1.7 on 2023-03-24 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_project_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 3, 24, 10, 49, 43, 488872, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='make',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 3, 24, 10, 49, 46, 114027, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='make',
            name='desc',
            field=models.CharField(default=datetime.datetime(2023, 3, 24, 10, 49, 55, 561599, tzinfo=datetime.timezone.utc), max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='make',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='model',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 3, 24, 10, 49, 57, 857284, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model',
            name='desc',
            field=models.CharField(default=datetime.datetime(2023, 3, 24, 10, 50, 2, 811885, tzinfo=datetime.timezone.utc), max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='part',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 3, 24, 10, 50, 7, 567571, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 3, 24, 10, 50, 9, 299580, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 3, 24, 10, 50, 11, 208218, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='part',
            name='desc',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='project',
            name='desc',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.CharField(max_length=10000),
        ),
    ]
