from django.shortcuts import render

# Create your views here.
def index(request):
    # print(request)
    # pass
    context = {
    }
    return render(request, "index.html", context)

def profile(request):
    # print(request)
    # pass
    context = {
    }
    return render(request, "profile.html")