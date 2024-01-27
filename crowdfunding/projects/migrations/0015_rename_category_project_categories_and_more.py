# Generated by Django 4.2.3 on 2024-01-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_rename_categories_project_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category',
            new_name='categories',
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(choices=[('Crisis Response and Relief', 'Crisis Response and Relief'), ('Innovation for Social Impact', 'Innovation for Social Impact'), ('Community Resilience', 'Community Resilience'), ('Equity and Inclusion', 'Equity and Inclusion'), ('Tech for Good', 'Tech for Good'), ('Education Access', 'Education Access'), ('Food Security', 'Food Security'), ('Environmental Stewardship', 'Environmental Stewardship'), ('Sustainable Development', 'Sustainable Development'), ('Clean Energy Initiatives', 'Clean Energy Initiatives'), ('Animal Welfare', 'Animal Welfare'), ('Community Empowerment', 'Community Empowerment'), ('Health and Wellness', 'Health and Wellness')], max_length=200),
        ),
    ]
