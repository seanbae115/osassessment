from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Users


def home(request):
    context = {'user_list': Users.objects.all()}
    return render(request, 'home.html', context)


def register_user(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = UserForm()
        else:
            user = Users.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, 'form.html', {'form': form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = Users.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('home')


def delete(request, id):
    user = Users.objects.get(pk=id)
    user.delete()
    return redirect('home')
