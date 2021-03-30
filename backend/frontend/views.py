from django.core import serializers
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse
from frontend.models import Person


@require_http_methods(["GET"])
def add_person(request):
    response = {}
    try:
        person = Person(user_name=request.GET.get('user_name'))
        person.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_person(request):
    response = {}
    try:
        person = Person.objects.filter()
        print(json.loads(serializers.serialize("json", person)))
        response['list'] = json.loads(serializers.serialize("json", person))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
