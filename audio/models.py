from django.db import models
from accounts.models import User
from aawaj import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "category"
    
    def __str__(self):
        return self.name


class AudioBooks(models.Model):
    book_name = models.CharField(max_length=255,)
    book_author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    speaker = models.CharField(max_length=255)
    publication = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    pdf_file = models.FileField(blank=True, null=True, upload_to="audio_book/pdf")
    publish_date = models.DateField()
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    album = models.ImageField(upload_to="audio_book/album", null=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name_plural = "AudioBooks"
        verbose_name = "AudioBook"


class Chapters(models.Model):
    audio_book = models.ForeignKey(AudioBooks, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    audio_file = models.FileField(upload_to="audio_book/chapters/audio_file")
    album = models.ImageField(upload_to="audio_book/Chapters/album")

    class Meta:
        verbose_name_plural = "Chapters"
        verbose_name = "Chapter"
    
    def __str__(self):
        return self.title
