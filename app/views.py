from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

def keyboard(request):
    return JsonResponse(
        {
        'type':'text'
        }
    )

@crsf_protect
def message(request):
    return JsonResponse(
        {
            'message':{
                'text': '메세지 동작'
            },
            'keyboard':{c
                'type':'text'
            }
        }
    )
