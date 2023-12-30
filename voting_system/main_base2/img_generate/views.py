from django.shortcuts import render ,HttpResponse

# Create your views here.
def image(request):
    return render(request , "image.html")
