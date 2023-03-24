from django.shortcuts import render

# Create your views here.
def hola(request):
    info = {
        'name' : 'juaang',
        'age' : 21
    }
    return render(request, 'myapp/hola.html', {'info': info})