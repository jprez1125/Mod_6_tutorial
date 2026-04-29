from urllib import request

from django.shortcuts import render

from django.shortcuts import render
from .forms import NameForm

def index(request):
    context = {
        "message": "hello from Django!",
        "items": ["Apples", "Bananas", "Cherries"]
    }
    return render(request, "tutorialapp/index.html", context)

def form_view(request):
    submitted_name = None
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            submitted_name = form.cleaned_data["name"]
    else:
        form = NameForm()

    return render(request, "tutorialapp/form.html", {
        "form": form,
        "submitted_name": submitted_name
    })