from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, default='Short title of your problem')
    description = models.TextField(max_length=3000)
    slug = models.SlugField(max_length=140, unique=True)
    date = models.DateTimeField(null=True, default=timezone.now())
    category = models.ForeignKey(Category, null=True, default=None)
    satisfied = models.BooleanField(default=False)
    viewed = models.IntegerField(default=0)
    
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
    satisfied = models.BooleanField(default=False)
    irrelevant = models.BooleanField(default=False)

    def __str__(self):
        return self.question.title


# request topics
class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    date = models.DateField(auto_now_add = True, null=True)


    def __str__(self):
        return self.title

# notifications
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    any_message = models.CharField(max_length=500, null=True, default="Notification")
    date = models.DateField(default=timezone.now())
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username