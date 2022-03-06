from django.shortcuts import render

# Login page
def front_page(request):
    return render(request, 'front_layout.html', {})

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html',{})