from django.contrib import admin
from .models import *

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)

admin.site.register(Topic)