# Generated by Django 4.2.3 on 2024-01-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_pledge_supporter_alter_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
