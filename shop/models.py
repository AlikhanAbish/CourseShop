from audioop import reverse

from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', default=None, blank=True, null=True, verbose_name='Photo')
    students_qty = models.IntegerField(blank=True, null=True)
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class UploadFiles(models.Model):
    file=models.FileField(upload_to='uploads_model')