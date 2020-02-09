from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save(commit=False)
            user.save()
            messages.success(request, f'Welcome {username}, your account is created')
            
            return redirect('timeline:index')
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form':form})