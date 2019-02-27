# Django Model Forms 1

## Lecture:
Discuss model (bound) forms

### Exercise 1:
Code together basic User signup page:

```
# models.py

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, unique=True)

```

```
# forms.py

from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

```

```
# views.py

from django.shortcuts import render

# Create your views here.
from .forms import NewUserForm

# Basic landing page
def index(request):
    return render(request, 'appTwo/index.html')

# User form for collecting User data 
def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'appTwo/users.html', {'form': form})

```

```
# appTwo/users.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Users</title>
</head>
<body>
<h1>Please Sign up Here!</h1>
    <form method="POST">
        {{ form.as_p }}
        {% csrf_token %}
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
