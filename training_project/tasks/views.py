from django.core import serializers
from django.shortcuts import render, HttpResponse
from tasks.models import Task


def index(request):
    return render(request, 'tasks/index.html', {'tasks': Task.objects.all()})


def api(request):
    id = request.GET['id']
    try:
        data = serializers.serialize('json', Task.objects.get(pk=id).get_descendants(include_self=True))
    except Task.DoesNotExist:
        return HttpResponse("Invalid id")
    return HttpResponse(data, content_type='application/json')
