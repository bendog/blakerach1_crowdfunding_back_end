# Generated by Django 4.2.3 on 2024-01-21 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_pledge_supporter_alter_project_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('COE', 'Community Empowerment'), ('ENS', 'Environmental Stewardship'), ('EDA', 'Education Access'), ('HEW', 'Health and Wellness'), ('EQI', 'Equity and Inclusion'), ('INS', 'Innovation for Social Impact'), ('SUD', 'Sustainable Development'), ('CRR', 'Crisis Response and Relief'), ('TEG', 'Tech for Good'), ('ANW', 'Animal Welfare'), ('CEI', 'Clean Energy Initiatives'), ('FOS', 'Food Security'), ('COR', 'Community Resilience')], max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('project', models.ManyToManyField(to='projects.project')),
            ],
        ),
    ]