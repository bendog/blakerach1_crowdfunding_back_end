# Generated by Django 4.2.3 on 2024-01-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_categories_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='pledge_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(choices=[('Community Empowerment', 'Community Empowerment'), ('Tech for Good', 'Tech for Good'), ('Environmental Stewardship', 'Environmental Stewardship'), ('Equity and Inclusion', 'Equity and Inclusion'), ('Health and Wellness', 'Health and Wellness'), ('Innovation for Social Impact', 'Innovation for Social Impact'), ('Education Access', 'Education Access'), ('Sustainable Development', 'Sustainable Development'), ('Animal Welfare', 'Animal Welfare'), ('Community Resilience', 'Community Resilience'), ('Food Security', 'Food Security'), ('Crisis Response and Relief', 'Crisis Response and Relief'), ('Clean Energy Initiatives', 'Clean Energy Initiatives')], max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]