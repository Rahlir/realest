# Generated by Django 5.0.1 on 2024-01-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('location', models.CharField()),
                ('image_link', models.CharField()),
                ('insertion_order', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'postings',
                'ordering': ['insertion_order'],
            },
        ),
    ]
