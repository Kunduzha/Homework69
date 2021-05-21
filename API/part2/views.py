import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse

from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def calculate_numbers(request, *args):
    if request.method == 'GET':
        return HttpResponse(json.dumps({'token': "ok"}))
    return HttpResponseNotAllowed('Only GET request are allowed')


def add(request):
    if request.method=='POST':
       body = request.body
       data = json.loads(body)
       if not data.get("A") or not data.get('B'):
           response = JsonResponse({'error': 'Введите что нибудь!!'})
           response.status_code = 400
           return response
       try:
            result = int(data['A']) + int(data['B'])
            return JsonResponse({'result': result})
       except:
           response = JsonResponse({'error': "Ввести нужно только числа"})
           response.status_code = 400
           return response



def subtruct(request):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        if not data.get("A") or not data.get('B'):
            response = JsonResponse({'error': 'Введите что нибудь!!'})
            response.status_code = 400
            return response
        try:
            result = int(data['A']) - int(data['B'])
            return JsonResponse({'result': result})
        except:
            response = JsonResponse({'error': "Ввести нужно только числа"})
            response.status_code = 400
            return response

def multiply(request):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        if not data.get("A") or not data.get('B'):
            response = JsonResponse({'error': 'Введите что нибудь!!'})
            response.status_code = 400
            return response
        try:
            result = int(data['A']) * int(data['B'])
            return JsonResponse({'result': result})
        except:
            response = JsonResponse({'error': "Ввести нужно только числа"})
            response.status_code = 400
            return response

def divide(request):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        if not data.get("A") or not data.get('B'):
            response = JsonResponse({'error': 'Введите что нибудь!!'})
            response.status_code = 400
            return response
        try:
            result = int(data['A']) / int(data['B'])
            return JsonResponse({'result': result})
        except:
            response = JsonResponse({'error': "Ввести нужно только числа"})
            response.status_code = 400
            return response