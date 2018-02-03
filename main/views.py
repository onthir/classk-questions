from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import *
import datetime
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from collections import Counter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.utils import timezone
from account.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max

# Create your views here.

def home(request):
    questions = Question.objects.all().order_by("-date")

    # counting answers on specific questions
    results = Question.objects.annotate(num_answers=Count('answer')).order_by("-date")

    # PAGINATION ===============================
    page = request.GET.get('page', 1)

    paginator = Paginator(results,4)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
   
    # end of counting
    empty = []
    for a in  Answer.objects.all():
        idd = a.id
        question_id = (a.question_id)
        empty.append(str(question_id))
    repeatition = Counter(empty)
    i = 0
    trend_list = []
    for x in range(len(repeatition)):
        new = repeatition.most_common()[i][0]
        trend_list.append(new)
        i += 1
    if len(trend_list) != 0:
        trend = Question.objects.get(id=trend_list[0])
    else:
        trend = None
    # getting the answers to all questions in the front page

    # search the questions ============
    query= request.GET.get("q")
    if query:
        short_list = Question.objects.all()
        questions = short_list.filter(title__icontains=query)
        resulted = questions.annotate(num_answers=Count('answer'))
        counted = questions.count()
        context1 = {
            'questions': questions,
            'query': query,
            'counted': counted,
            'resulted': resulted,
        }
        return render(request, 'main/search.html',context1)
    context = {
        'questions': questions,
        'trend': trend,
        'results': results,        
    }
    return render(request, 'main/index.html', context)

# ask questions
@login_required(redirect_field_name='classk_redirect')
def question(request):
    if request.user.is_authenticated:
        lists = Category.objects.all().order_by("category")
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            user = request.user
            date =  timezone.now()
            vl = request.POST.get('values')
            category_item = Category.objects.get(category=vl)
            questionobj = Question(user=user, title=title, description=description, date=date, category=category_item)
            questionobj.save()
            return redirect('main:home')
        else:
            form = QuestionForm()
        return render(request, 'main/ask-question.html', {'form': form,'lists':lists, })
    else:
        return redirect('accounts:login')

# details for the question
def details(request, slug):
    question = Question.objects.get(slug=slug)
    answers = Answer.objects.filter(question_id=question.id)
    cot = answers.count()
    # similar questions
    similar = Question.objects.filter(category=question.category)
    final = similar.exclude(title=question.title).order_by('-date')[:5]

    # adding the views
    initial_views = 0
    question.viewed = int(question.viewed) + 1
    question.save()
    
    viewed = question.viewed
    # questions by that user
    questions_by_the_user = Question.objects.filter(user=question.user).count()

    # answers with mark satisfied
    satisfied_answers = Answer.objects.filter(question_id = question.id, satisfied=True)
    no_review_answers = Answer.objects.filter(question_id=question.id, satisfied=False)

    # categories
    cats = Category.objects.all()[:5]
    context = {
        'question': question,
        'answers':answers,
        'cot': cot,
        'final': final,
        'questions_by_the_user': questions_by_the_user,
        'viewed': viewed,
        'satisfied_answers': satisfied_answers,
        'no_review_answers': no_review_answers,
        'cats':cats,
    }
    return render(request, 'main/detail.html', context)

# delete question
def delete(request, slug):
    if request.user.is_authenticated():
        instance = get_object_or_404(Question, slug=slug)
        if request.user == instance.user:
            instance.delete()
            messages.success(request, 'Question Deleted Successfully!')  # <-
            return redirect('main:home')
        else:
            return redirect('main:home')

# edit question
def edit_details(request, slug):
    if request.user.is_authenticated:
        question = Question.objects.get(slug=slug)
        if request.user == question.user:
            if request.method == 'POST':
                form = QuestionForm(request.POST, instance=question)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Question Edited Successfully!')  # <-
                    return HttpResponseRedirect('/details/%s' %slug)
            else:
                form = QuestionForm(instance=question)
            template = 'main/edit-question.html'
            context = {'form': form}
            return render(request, template, context)
        else:
            return redirect("main:home")
    else:
        return redirect("main:home")


# answer to the question
def answer(request, slug):
    if request.user.is_authenticated():
        questions = Question.objects.get(slug=slug)
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.user = request.user
                answer.question = questions
                answer.posted_on = datetime.datetime.now().date()
                answer.save()
                return HttpResponseRedirect('/details/%s' %slug)
        else:
            form = AnswerForm(request.POST)
        return render(request, 'main/answer.html', {'form': form, 'questions': questions,})
    else:
        return redirect("accounts:login")

# update answer
def update_answer(request, slug, id):
    # test user login here
    if request.user.is_authenticated():
        quest = Question.objects.get(slug=slug)
        try:
            answer = Answer.objects.get(user=request.user, question_id=quest.id, id=id)
        except:
            return redirect("main:home")
        answer = Answer.objects.get(user=request.user, question_id=quest.id, id=id)
        new = (answer.answer)
        if request.user == answer.user:
            if request.method == 'POST':
                form = AnswerForm(request.POST or None, instance=answer)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/details/%s' %slug)
            else:
                form = AnswerForm(request.POST or None, instance=answer)
            return render(request, 'main/edit-answer.html', {'form': form, 'quest':quest})
        else:
            return redirect("main:home")

    else:
        return redirect("main:home")

# delete answer by the user
def delete_answer(request, slug, id):
    if request.user.is_authenticated():
        quest = Question.objects.get(slug=slug)
        try:
            answer = Answer.objects.get(user=request.user, question_id=quest.id, id=id)
        except:
            return redirect("main:home")
        if request.user == answer.user:
            if not answer.satisfied == True:
                answer.delete()
                messages.success(request, 'Answer Deleted Successfully!')
                return HttpResponseRedirect('/details/%s' %slug)
            else:
                return HttpResponseRedirect('/details/%s' %slug)
        else:
            return HttpResponseRedirect('/details/%s' %slug)



    else:
        return redirect("accounts:login")

def filter_types(request, tag):
    filters = Category.objects.get(category=tag)
    questions = Question.objects.filter(category=filters)[:1]
    questions_all = Question.objects.filter(category=filters)
    count_in_category = questions_all.count()
    return render(request, 'main/filtered.html', {'questions': questions, 'questions_all': questions_all, 'count_in_category': count_in_category})

# website tutorial
def tutorial(request):
    return render(request, 'main/website-tutorial.html')

# request a topic
def request_topic(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            user = request.user
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            date = datetime.datetime.now()
            topic = Topic(user=user, title=title, description=desc, date=date)
            topic.save()
            return redirect('main:display_request')
        else:
            return render(request, 'main/topic.html')
        return render(request, 'main/topic.html', {'topic':topic})
    else:
        return redirect('main:home')

# display the topic requestS
def display_request(request):
    requests = Topic.objects.all().order_by("-date")

    context = {
        'requests': requests,
        
    }
    return render(request, 'main/display-topic.html', context)

# answer satisfied
def satisfied(request, slug, id, *args, **kwargs):
    if request.user.is_authenticated():
        question = Question.objects.get(slug=slug)
        answer = Answer.objects.get(question_id=question.id, id=id) #and get the specific answer id or something
        profile = Profile.objects.get(user=answer.user)
        profileb = Profile.objects.get(user=question.user)
        # answer user points
        answer_user_points = profile.points

        # question user points
        question_user_points = profileb.points
        if request.user == question.user:
            question.satisfied = True
            answer.satisfied = True

            # increasing answer user points
            profile.points = int(answer_user_points) + 10

            # increasing question user points
            profileb.points = int(question_user_points) + 1

            profileb.save()
            profile.save()
            question.save()
            answer.save()
            return HttpResponseRedirect('/details/%s' %slug)
        else:
            return HttpResponseRedirect('/details/%s' %slug)
    else:
        return redirect("accounts:login")
        
# irrelevant answer
def out_of_context(request, slug, id, *args, **kwargs):
    if request.user.is_authenticated():
        question = Question.objects.get(slug=slug)
        answer = Answer.objects.get(question_id=question.id, id=id) #and get the specific answer id or something
        profile = Profile.objects.get(user=answer.user)
        profileb = Profile.objects.get(user=question.user)
        # answer user points
        answer_user_points = profile.points

        # question user points
        question_user_points = profileb.points
        if request.user == question.user:
            answer.irrelevant = True
            profile.points = int(answer_user_points) - 3
            answer.save()
            profile.save()
            return HttpResponseRedirect('/details/%s' %slug)
        else:
            return HttpResponseRedirect('/details/%s' %slug)
    else:
        return redirect("accounts:login")
            
# delete topics
def delete_topics(request, id):
    if request.user.is_superuser:
        topics = Topic.objects.get(id=id)
        topics.delete()
        return redirect("main:display_request")
    else:
        return redirect("main:display_request")

def add_categorys(request):
    if request.user.is_superuser:
        topics = Category.objects.all().order_by("category")
        message = "Category already exists."
        if request.method == 'POST':
            form = CategoryForm(request.POST or None)
            if form.is_valid():
                topic = form.save(commit=False)
                if Category.objects.filter(category=topic).exists():
                    return message
                else:
                    topic.category = topic.category.replace(" ", "-")
                    topic.save()
                return redirect('main:add-category')
        else:
            form = CategoryForm(request.POST or None)
        return render(request, 'main/add-category.html', {'form':form, 'topics':topics, 'message':message})
    else:
        return redirect("main:home")

# undo the satisfied
def undo_satisfied(request, slug, id, *args, **kwargs):
    if request.user.is_authenticated():
        question = Question.objects.get(slug=slug)
        answer = Answer.objects.get(question_id=question.id, id=id) #and get the specific answer id or something
        profile = Profile.objects.get(user=answer.user)
        profileb = Profile.objects.get(user=question.user)
        # answer user points
        answer_user_points = profile.points

        # question user points
        question_user_points = profileb.points
        if request.user == question.user:
            question.satisfied = False
            answer.satisfied = False

            # increasing answer user points
            profile.points = int(answer_user_points) - 10

            # increasing question user points
            profileb.points = int(question_user_points) - 1

            profileb.save()
            profile.save()
            question.save()
            answer.save()
            return HttpResponseRedirect('/details/%s' %slug)
        else:
            return HttpResponseRedirect('/details/%s' %slug)
    else:
        return redirect("accounts:login")
# undo irrelevant
def undo_out_of_context(request, slug, id, *args, **kwargs):
    if request.user.is_authenticated():
        question = Question.objects.get(slug=slug)
        answer = Answer.objects.get(question_id=question.id, id=id) #and get the specific answer id or something
        profile = Profile.objects.get(user=answer.user)
        profileb = Profile.objects.get(user=question.user)
        # answer user points
        answer_user_points = profile.points

        # question user points
        question_user_points = profileb.points
        if request.user == question.user:
            answer.irrelevant = False
            profile.points = int(answer_user_points) + 3
            answer.save()
            profile.save()
            return HttpResponseRedirect('/details/%s' %slug)
        else:
            return HttpResponseRedirect('/details/%s' %slug)
    else:
        return redirect("accounts:login")
user = []
points = []
def hall_of_fame(request):
    if request.user.is_authenticated():
        total_questions = Question.objects.all().count()
        total_answers = Answer.objects.all().count()
        total_users = User.objects.all().count()
        profiles = Profile.objects.all()
        for p in profiles:
            highest = p.points
            points.append(highest)
        ranked_1 = Profile.objects.get(points=sorted(points)[0])
        ranked_2 = Profile.objects.get(points=sorted(points)[1])

        # context for the hall of fame
        context = {
            'total_questions':total_questions,
            'total_answers': total_answers,
            'total_users': total_users,
            'ranked_1': ranked_1,
            'ranked_2': ranked_2,
        }
        return render(request, 'main/hall-of-fame.html',)
