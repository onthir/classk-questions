from django.contrib.sitemaps import Sitemap

from main.models import Question

class QuestionSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Question.objects.all()