from django.shortcuts import render

from .forms import NewUserForm, ContactForm


# Basic landing page
def index(request):
    return render(request, 'user_app/index.html')


# User form for collecting User data
def users(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'user_app/users.html', {'form': form})



