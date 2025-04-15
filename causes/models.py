from django.db import models
from django.utils.text import slugify

class Cause(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='causes/')
    description = models.TextField(max_length=300)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    progress = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.progress = int((self.raised_amount / self.goal_amount) * 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
