# Generated by Django 5.0.6 on 2024-06-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('roll', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
