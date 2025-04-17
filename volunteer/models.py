from django.db import models
from django.core.validators import MinLengthValidator


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    motivation = models.TextField(
        validators=[MinLengthValidator(20, "Please write at least 20 characters")]
    )
    submission_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.submission_date.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-submission_date']
        verbose_name = "Volunteer Application"
        verbose_name_plural = "Volunteer Applications"