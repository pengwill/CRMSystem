# Generated by Django 2.1.2 on 2018-10-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_orderinfo_is_rated'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteminfo',
            name='rate_times',
            field=models.IntegerField(default=1),
        ),
    ]