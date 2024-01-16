from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    COMMUNITY_ENGAGEMENT = "CE"
    ENVIRONMENTAL_STEWARDSHIP = "ES"
    EDUCATION_ACCESS = "EA"
    HEALTH_WELLNESS = "HW"
    PROJECT_CATEGORIES = {
        COMMUNITY_ENGAGEMENT: "Community Empowerment",
        ENVIRONMENTAL_STEWARDSHIP: "Environmental Stewardship",
        EDUCATION_ACCESS: "Education Access",
        HEALTH_WELLNESS: "Health and Wellness",
    }
    
    name = models.CharField(
        max_length=2,
        choices=PROJECT_CATEGORIES,
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    category = models.ManyToManyField(Category,null=True, blank=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )

# The related name specifies the name of the reverse relationship 

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )

