from django.db.models import Avg
from django.shortcuts import render, redirect
from .models import BookReview
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def reviews(request):
    reviews = BookReview.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'review/book_review.html', context)


def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return reviews(request)
    else:
        form = ReviewForm
    return render(request, 'review/review_form.html', {'form': form})

