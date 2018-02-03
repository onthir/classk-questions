from django import forms
from .models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('category','title', 'description',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)

class TopicForm(forms.ModelForm):
    title = forms.CharField(max_length=80, required=True)
    class Meta:
        model = Topic
        fields = ('title', 'description')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category',)