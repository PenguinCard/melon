from django.http import JsonResponse, HttpResponse


def index(request):
    if request.method == 'POST':
        return JsonResponse({'request': request.data})
    elif request.method == 'GET':
        return HttpResponse('test')
