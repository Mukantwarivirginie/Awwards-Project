from django.shortcuts import render


# Create your views here.
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Project,Profile
from .forms import SignUpForm,ProfileForm,ProjectForm
from django.contrib.auth.decorators import login_required

def awwards(request):
    projects = Project.objects.all()
    return render(request, 'photos/todays-projects.html', {"projects":projects})

def projects_of_day(request):
    projects = Project.todays_projects()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['your_title']
            description = form.cleaned_data['description']
            link = form.cleaned_data['link']
            recipient = SignUpRecipients(title = title,description = description,link = link)
            recipient.save()
            HttpResponseRedirect('projectsToday')
    else:
        form = SignUpForm()
    return render(request, 'all-projects/todays-projects.html',{"projects":projects,"signupForm":form})

    def project(request,project_id):
        try:
            project = Project.objects.get(id = project_id)
        except DoesNotExist:
            raise Http404()
        return render(request,"all-photos/todays-projects.html")






def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('new-profile')

    else:
        form = ProfileForm()
    return render(request, 'new-profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def view_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(email=current_user.email)
    print(profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_form = form.save(commit=False)
            profile_form.editor = current_user
            profile_form.save()

        return redirect('view-profile')

    else:
        form = ProfileForm()
    return render(request, 'view-profile.html', {"form": form,"profile":profile})


@login_required(login_url='/accounts/login/')
def addimage(request):

    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
   
        return redirect('awwards')

    else:
        form = ImageForm()
    return render(request, 'addimage.html', {"form": form})

@login_required(login_url='/accounts/login/')
def postproject(request):
    current_user = request.user
    if request.method == 'POST':
        form =  ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('Awwards')

    else:
        form =  ProjectForm()
    return render(request, 'photos/postproject.html', {"form": form})



def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})












