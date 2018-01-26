from django.shortcuts import render
from .models import Project, Tag, Screenshot


# Create your views here.


def index(request):

    projects = Project.objects.filter().all()

    return render(request, 'me/index.html', {'projects': projects})


def single_project(requests, project_name):

    try:

        project = Project.objects.get(name=project_name)

        tags = Tag.objects.filter(project=project).all()

        screenshots = Screenshot.objects.filter(project=project).all()

        return render(requests, 'projects/single-project.html', {'project': project, 'tags': tags,
                                                                 'screenshots': screenshots})

    except Exception as exception:

        raise exception


