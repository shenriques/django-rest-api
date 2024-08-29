from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs): # request -> HttpRequest class instance from django

    print(request.GET) # prints url query params
    body = request.body # byte string of json
    data = {}
    try:
        data = json.loads(body) # string of json data to python dict
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)