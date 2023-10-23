from django.shortcuts import render


def inicio(request):
    return render(request, "segundaApp/index.html")

def chile(request):
    data = {"nombre":"Selección de Chile", "fecha":"19 de junio de 1895.","copaA":"2","PcopaM":"9", "estadocl":"disabled"}
    return render(request, "segundaApp/index.html", data)

def brasil(request):
    data = {"nombre":"Seleção Brasileira de Futebol", "fecha":"21 de julio de 1914.","copaA":"9","PcopaM":"22", "estadobr":"disabled"}
    return render(request, "segundaApp/index.html", data)
def argentina(request):
    data = {"nombre":"Selección Argentina de Fútbol", "fecha":"21 de febrero de 1893.","copaA":"15","PcopaM":"17", "estadoar":"disabled"}
    return render(request, "segundaApp/index.html", data)