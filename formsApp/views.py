# formsApp/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UserRegistrationForm
from .models import UserData

def home(request):
    return render(request, 'index.html')

def manage_users(request, user_id=None):
    form = UserRegistrationForm()
    users = UserData.objects.all()

    if user_id:
        user = UserData.objects.get(id=user_id)
        form = UserRegistrationForm(instance=user)

        if request.method == 'POST':
            form = UserRegistrationForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('manage_users')
    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({
                        'id': user.id,
                        'nombre': user.nombre,
                        'email': user.email,
                        'fono': user.fono,
                    })
                return redirect('manage_users')

    return render(request, 'index.html', {'form': form, 'users': users, 'user_id': user_id})

def update_user(request, user_id):
    user = UserData.objects.get(id=user_id)
    form = UserRegistrationForm(instance=user)

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')

    return render(request, 'update_user.html', {'form': form, 'user_id': user_id})

def delete_user(request, user_id):
    user = UserData.objects.get(id=user_id)
    
    if request.method == 'POST':
        user.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'User deleted successfully'})
        return redirect('manage_users')

    return render(request, 'delete_user.html', {'user': user})
