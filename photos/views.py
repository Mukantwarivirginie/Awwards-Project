from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Project,Profile
from .forms import SignUpForm

def Awward(request):
     return render(request, 'Awward.html')

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


def search_results(request):

    if 'postname' in request.GET and request.GET["postname"]:
        search_term = request.GET.get("postname")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"message":message})


