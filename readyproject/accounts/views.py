from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # optional, for showing errors
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        # 1️⃣ Get username and password from the form
        username = request.POST['username']
        password = request.POST['password']

        # 2️⃣ Authenticate user
        user = authenticate(request, username=username, password=password)

        # 3️⃣ Check if authentication succeeded
        if user is not None:
            # 4️⃣ Login user → creates session
            login(request, user)

            # 5️⃣ Redirect to dashboard (or protected page)
            return redirect('dashboard')
        else:
            # 6️⃣ Authentication failed → show message
            messages.error(request, "Invalid username or password")
            return redirect('login')  # reload login page

    else:
        # 7️⃣ GET request → show empty login form
        return render(request, 'accounts/login.html')
    
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def user_logout(request):
    logout(request)
    return redirect('login')

    
