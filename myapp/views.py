# myapp/views.py
from django.shortcuts import render, redirect
from .forms import UserForm

def home(request):
    return render(request, "home.html")

def submit(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('registration_success') # Redirect to a success page
        else:
            # If the form is not valid, you might want to render the form again
            # with the errors to show the user.
            return render(request, 'home.html', {'form': form})
    else:
        # If someone tries to access this URL with a GET request,
        # you might want to redirect them or display an error.
        return redirect('home') # Or handle it differently

def registration_success(request):
    return render(request, 'registration_success.html') # Create this template