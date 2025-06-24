

# app1/views.py
from django.shortcuts import render
from alpno.forms import MyForm  # Import your form

def t(request):
    form = MyForm()  # Create an instance of your form
    #return render(request, 'app1/index.html', {'form': form})  # Pass it to the template
    return render(request, 'app1/base.html', {'form': form})