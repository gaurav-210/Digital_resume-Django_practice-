from django.http import HttpResponse       # Returns response
from django.shortcuts import render     # To render to a template ..





def GauravPage(request):      # Request response ..
    return render(request, "resume.html" , {})

def Gaurav(request):      # Request response ..
    return render(request, "food.html" , {})

