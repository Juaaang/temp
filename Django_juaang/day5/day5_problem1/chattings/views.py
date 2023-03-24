from django.shortcuts import render, redirect
from .models import Chat
from .forms import ChatForm
# Create your views here.
def index(request):
    chattings = Chat.objects.all()
    context ={'chattings':chattings}
    return render(request, 'chattings/index.html', context)

def create(request):
    if request.method =='POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            content = form.cleaned_data['content']
            chatting = Chat(user=user, content=content)
            chatting.save()
            return redirect('chattings:detail', chatting.pk)
    form = ChatForm()
    context={'form':form}
    return render(request, 'chattings/create.html', context)

def detail(request, pk):
    chatting = Chat.objects.get(pk=pk)
    context={'chatting':chatting}
    return render(request, 'chattings/detail.html', context)