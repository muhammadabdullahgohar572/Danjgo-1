from django.http import HttpResponse
from django.shortcuts import render
def Home(request):
    return render(request, 'web/index.html')




def About(request):
    return HttpResponse("About Us Page")

def Contact_us(request):
    return HttpResponse("Contact Us Page")
