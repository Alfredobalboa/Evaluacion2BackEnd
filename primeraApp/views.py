from django.shortcuts import render

def renderView(request):
    return render(request, "primeraApp/index.html")