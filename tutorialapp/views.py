from urllib import request
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from .forms import NameForm, CommentForm
from .models import Comment
from django.contrib import messages
def index(request):
    context = {
        "message": "hello from Django!",
        "items": ["Apples", "Bananas", "Cherries"]
    }
    return render(request, "tutorialapp/index.html", context)


@login_required
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

def about(request):
    """Render the about page with a message."""
    return render(request, "tutorialapp/about.html", {
        "message": "This is the about page."
    })

def comments(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " comment was submitted successfully")
            return redirect("comments")
    else:
        form = CommentForm()

    approved_comments = Comment.objects.filter(approved=True)

    return render(request, "tutorialapp/comments.html", {
        "form": form,
        "comments": approved_comments

    })