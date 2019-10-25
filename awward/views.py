from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Project,Profile,rate
from .forms import NewProjectForm,ProfileForm,RateForm
import datetime as dt


# Create your views here.
def welcome(request):
    projects = Project.objects.all().order_by("-id")
    profiles= Profile.objects.all()
    current_user = request.user
    return render(request, 'welcome.html',{"projects":projects,"profiles":profiles,"current_user":current_user,})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    user_object = request.user
    current_user = Profile.objects.get(username__id=request.user.id)
    user = Profile.objects.get(username__id=id)
    projects = Project.objects.filter(upload_by = user)
    projects = Project.objects.all()
    return render(request, "profile.html", {"current_user":current_user,"projects":projects,"user":user,"user_object":user_object})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = Profile.objects.get(username__id=request.user.id)
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.upload_by = current_user
            project.save()
        return redirect('welcome')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

   


