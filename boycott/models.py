# models.py
from django.db import models


class Alternative(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class BoycottCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")

    def __str__(self):
        return self.name


class BoycottTarget(models.Model):
    BOYCOTT_LEVELS = [
        (1, 'Avoid if possible'),
        (2, 'Significant ties to occupation'),
        (3, 'Direct weapons supplier'),
    ]

    name = models.CharField(max_length=200)
    category = models.ForeignKey(BoycottCategory, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='boycott/logos/', blank=True)
    description = models.TextField()
    alternatives = models.ManyToManyField(Alternative, blank=True)
    level = models.IntegerField(choices=BOYCOTT_LEVELS)
    verified = models.BooleanField(default=False)
    last_updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-level', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"





class UserReport(models.Model):
    target = models.ForeignKey(BoycottTarget, on_delete=models.CASCADE)
    evidence = models.URLField()
    submitted_by = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
    date_submitted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Report on {self.target.name}"