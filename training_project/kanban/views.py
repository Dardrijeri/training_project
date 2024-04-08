from django.shortcuts import HttpResponse
from django.core import serializers
from kanban.models import Task
from django.views.decorators.csrf import csrf_exempt
import json


def api(request):
    return HttpResponse(Task.objects.all().values())


@csrf_exempt
def data(request):
    data = json.dumps(list(Task.objects.all().values()))
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def insert(request):
    value = json.loads(request.body)
    print(value)
    Task.objects.create(Id=value['value']['Id'], status=value['value']['Status'], description=value['value']['Summary'],
                        executor=value['value']['Assignee'])
    data = json.dumps(list(Task.objects.all().values()))
    print(data)
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def delete(request):
    value = json.loads(request.body)
    Task.objects.filter(pk=value['key']).delete()
    data = json.dumps(list(Task.objects.all().values()))
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def update(request):
    new_value = json.loads(request.body)
    Task.objects.filter(pk=new_value['value']['Id']).update(status=new_value['value']['status'])
    data = json.dumps(list(Task.objects.all().values()))
    return HttpResponse(data, content_type='application/json')
