from django.shortcuts import render
from django.http import JsonResponse
from .models import Greeting

def index(request):
    return render(request, 'greetings/index.html')

def get_greeting(request, surname_id):
    try:
        greeting = Greeting.objects.get(surname_id=surname_id)
        data = {
            'first_name': greeting.first_name,
            'message': greeting.message,
            'photo_url': greeting.photo.url if greeting.photo else None
        }
        return JsonResponse(data)
    except Greeting.DoesNotExist:
        return JsonResponse({'error': 'Greeting not found'}, status=404)
