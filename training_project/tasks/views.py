from django.core import serializers
from django.shortcuts import render, HttpResponse
from tasks.models import Task


def index(request):
    return render(request, 'tasks/index.html', {'tasks': Task.objects.all()})


def api(request):
    task_id = request.GET['id']
    try:
        data = serializers.serialize('json', Task.objects.get(pk=task_id).get_descendants(include_self=True))
    except Task.DoesNotExist:
        return HttpResponse("Invalid id")
    response = HttpResponse(data, content_type='application/json')

    # workaround to avoid including cors library
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return response
