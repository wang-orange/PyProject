from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json

# Create your views here.
def Login(request):
    result = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        date = request.POST.get('date')
        result['user'] = username
        result['pwd'] = pwd
        result['date'] = date
        results = json.dumps(result)
        return HttpResponse(results)
    # if request.method == 'GET':
    #     username = request.GET.get('username')
    #     pwd = request.GET.get('password')
    #     date = request.GET.get('date')
    #     result['user'] = username
    #     result['pwd'] = pwd
    #     result['date'] = date
    #     results = json.dumps(result)
    #     return HttpResponse(results)
    else:
        return render_to_response('login.html')