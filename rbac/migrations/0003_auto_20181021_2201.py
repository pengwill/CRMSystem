# Generated by Django 2.1.2 on 2018-10-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_menu_permission_role_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='database_id',
            field=models.IntegerField(default=1),
        ),
    ]
