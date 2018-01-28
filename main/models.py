from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    CATEGORY_CHOICES = (
        ('Math', 'Math'),
        ('Geography', 'Geography'),
        ('Biology', 'Biology'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Health', 'Health'),
        ('Computer-Science', 'Computer-Science'),
        ('History', 'History'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    slug = models.SlugField(max_length=140, unique=True)
    date = models.DateTimeField(null=True, default=timezone.now())
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default=None, null=True)
    satisfied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Question.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None)
    answer = models.TextField(max_length=3000, null=True)
    posted_on = models.DateField(default=datetime.datetime.now().date())

# request topics
class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    date = models.DateField(auto_now_add = True, null=True)

    def __str__(self):
        return self.title