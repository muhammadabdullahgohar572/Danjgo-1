from django.http import HttpResponse

def Home(request):
    return HttpResponse("Welcome to Home Page")

def About(request):
    return HttpResponse("About Us Page")

def Contact_us(request):
    return HttpResponse("Contact Us Page")
