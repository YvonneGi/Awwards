from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Project,Profile,Rate
from .forms import NewProjectForm,ProfileForm,RateForm
import datetime as dt
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  ProfileMerch
from .serializer import MerchSerializer



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
def new_project(request):
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


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    user_edit = Profile.objects.get(username__id=current_user.id)
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
                   
    else:
        form=ProfileForm(instance=request.user.profile)
     
    return render(request,'edit_profile.html',locals())

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_projects = Project.search_project(search_term)
        message=f"Search results for: {search_term}"

        return render(request,'search.html',{"message":message,"projects":searched_projects})

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = ProfileMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

   


