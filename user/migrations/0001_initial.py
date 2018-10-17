# Generated by Django 2.1.2 on 2018-10-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=64)),
                ('representative', models.CharField(max_length=32)),
                ('postcode', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=64)),
                ('apartment', models.CharField(max_length=32)),
                ('agent', models.CharField(max_length=32)),
                ('telephone', models.CharField(max_length=32)),
                ('bank', models.CharField(max_length=32)),
                ('taxid', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='StaffMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=32)),
                ('apartment', models.CharField(max_length=32)),
                ('role', models.CharField(max_length=32)),
                ('address', models.CharField(blank=True, max_length=64, null=True)),
                ('rate', models.FloatField(default=10.0)),
            ],
        ),
    ]