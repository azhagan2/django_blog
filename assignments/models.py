from django.db import models


class About(models.Model):
    about_title = models.CharField(max_length=200, default="About Me")
    about_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About' 

    def __str__(self):
        return self.about_title

class SocialMedia(models.Model):
    platform = models.CharField(max_length=100, default="Facebook") # e.g., Instagram, Twitter
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Social Media' 

    def __str__(self):
        return self.platform