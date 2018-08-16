from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.clean_password2()
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return redirect('libraryapp:index')
            # return HttpResponse(f'User:{user}, Pass:{password}')
        else:
            return HttpResponse("Invalid Form")
    context = {
    'form':UserCreationForm()
    }
    return render(request, 'registration/register.html', context)
