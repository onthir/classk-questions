from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from .forms import SignUpForm, UpdateProfileForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from main.models import *
from django.contrib import messages

def register(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.bio = request.POST.get('bio')
                user.profile.full_name = request.POST.get('full_name')
                user.profile.location = request.POST.get('location')
                user.profile.email = request.POST.get('email')
                user.profile.gender = request.POST.get('gender')
                user.profile.birth_date = request.POST.get('birth_date')
                user.profile.points = 10
    
                user.profile.save()
                raw_password = form.cleaned_data.get('password1')
            
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)

                messages.success(request, 'Welcome To Classk') 
                return redirect('main:home')
            else:
                return render(request, 'account/register.html', {'error_message': ' Invalid Username or Password ', 'form':form,})

        else:
            form = SignUpForm()
        return render(request, 'account/register.html', {'form': form})

# extending the user model to contain other details for the user


#login
def login_user(request):

    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main:home')
                else:
                    return render(request, 'account/login.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'account/login.html', {'error_message': 'Invalid username or password'})
        return render(request, 'account/login.html')

# logout user
def logout_user(request):
    logout(request)
    url = reverse("accounts:login")
    return redirect(url, args=(),kwargs={})

# user profile

def profile(request, user):
    
    global visits
    global points
    
    points = []
    visits = []
    
    profile = User.objects.get(username=user)
    details = Profile.objects.get(user_id=profile.id)

    # user stats asked, answered and most recent questions
    all_questions = Question.objects.filter(user_id=profile.id)
    asked = Question.objects.filter(user_id=profile.id).count()
    all_answers_by_the_user = Answer.objects.filter(user_id=profile.id)
    answered = Answer.objects.filter(user_id=profile.id).count()
    recent = Question.objects.filter(user_id=profile.id).order_by('-date')[0:3]

    # increasing the profile views
    view_count = details.viewes + 1
    details.viewes = view_count
    details.save() 
    new_data = details.viewes
    # getting recent answers by the user
    recent_answers = Answer.objects.filter(user_id=profile.id).order_by('-posted_on')[0:3]

    # rank of that user
    all_profile = Profile.objects.all()
    for p in all_profile:
        point = p.points
        points.append(point)
    ranks_in_order = sorted(points)
    highest_to_lowest =  (sorted(ranks_in_order, key=int, reverse=True))

    index_of_users_points = highest_to_lowest.index(details.points) 
    length_of_list = len(points)

    rank = (index_of_users_points/length_of_list)*100
    rank_title = "Top " + str(rank) + "% with rank " + str(index_of_users_points + 1)
    ranked = index_of_users_points + 1

    # highest profile visits
    all_profile_views = Profile.objects.all()
    for a in all_profile_views:
        v = a.viewes
        visits.append(v)
    visit_sorted = sorted(visits)
    descend = sorted(visit_sorted, key=int, reverse=True)

    index_of_users_visits = descend.index(details.viewes) + 1

    # satisfied answers by the user
    all_answers = Answer.objects.filter(user_id=profile.id)
    sat_ans = all_answers.filter(satisfied=True)
    irrelevant_ans = all_answers.filter(satisfied=False)
    print(sat_ans)
    print(irrelevant_ans)
    context = {
        'profile': profile,
        'details': details,
        'asked': asked,
        'answered': answered,
        'recent':recent,
        'recent_answers': recent_answers,
        'new_data': new_data,
        'all_questions':all_questions,
        'rank_title':rank_title,
        'index_of_users_points': index_of_users_points,
        'ranked':ranked,
        'index_of_users_visits': index_of_users_visits,
        'sat_ans':sat_ans,
        'irrelevant_ans':irrelevant_ans,
    }
    return render(request, 'account/profile.html', context)

# update profile
def update_profile(request, user):
    if request.user.is_authenticated:
        user_info = User.objects.get(username=user)
        profile = Profile.objects.get(user_id=user_info.id) 
        if request.user == profile.user:
            if request.method == 'POST':
                form = UpdateProfileForm(request.POST or None, instance=profile)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/accounts/profile/%s' %user)
            else:
                form = UpdateProfileForm(request.POST or None, instance=profile)
            return render(request, 'account/update-account.html', {'form': form})
        else:
            return redirect('main:home')
    else:
        return redirect("main:home")
