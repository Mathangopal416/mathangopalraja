# comments/views.py

from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
import random

def classify_comment(text):
    # Dummy spam classifier
    if 'spam' in text.lower():
        return 'Spam'
    elif 'buy now' in text.lower():
        return 'Suspicious'
    return 'Safe'

def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.label = classify_comment(comment.content)
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()

    comments = Comment.objects.order_by('-timestamp')
    return render(request, 'comments/index.html', {'form': form, 'comments': comments})
