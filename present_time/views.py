from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from time import gmtime, strftime, localtime
# Create your views here.

def main(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request,'index.html', context)

def alternative(request):
	pass


