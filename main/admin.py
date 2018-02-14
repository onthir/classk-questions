from django.contrib import admin
from .models import *
from django.http import HttpResponse
import decimal, csv


# Register your models here.
def export_questions(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="questions.csv"'
    writer = csv.writer(response)
    writer.writerow(['User', 'Title',  'Date', 'Description', 'Date', 'Category',])
    questions = queryset.values_list('user', 'title', 'description', 'date', 'category',)
    for q in questions:
        writer.writerow(q)
    return response
export_questions.short_description = 'Export to csv'

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'date')
    list_filter = ('user', 'category', 'date')
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    actions = [export_questions, ]


admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Notification)