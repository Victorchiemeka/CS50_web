from django.shortcuts import render
from django import forms

tasks = ["Alx", "CS50", "God"]

class Newtaskform(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label = "numbers", min_value=1, max_value=10)



# Create your views here.
def index(request):
    return render(request, "tasks/index.html",{
        "tasks": tasks
    })
def add(request):
    return render(request, "tasks/add.html",{
        "form": Newtaskform()
    })