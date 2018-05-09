from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def keyboard(request):
    return JsonResponse(
        {
        'type':'text'
        }
    )

@crsf_exempt
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
