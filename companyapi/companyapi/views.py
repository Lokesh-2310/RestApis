from django.http import HttpResponse,JsonResponse
def home_page(request):
    data={
        'hey':23,
        24:34
    }
    return JsonResponse(data,safe=False)