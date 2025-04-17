from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='events/')
    date = models.DateField(validators=[MinValueValidator(timezone.now().date())])
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.date}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        ordering = ['date']