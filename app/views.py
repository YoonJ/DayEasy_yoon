from django.shortcuts import render
from django.http import JsonResponse

def keyboard(request):
    return JsonResponse(
        {
        'type':'text'
        }
    )

def message(request):
    return JsonResponse(
        {
            'message':{
                'text': '메세지 동작'
            },
            'keyboard':{
                'type':'text'
            }
        }
    )
