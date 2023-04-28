from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.apps import apps


# Create your views here.

def home(request):
    return render(request, 'book/home.html')


@login_required
def upload_view(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'book/books.html', context)


@login_required
def upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'{title} was uploaded successfully!')
            return redirect('books/')
    else:
        form = BookForm
    return render(request, 'book/upload.html', {'form': form})


def book_details(request, pk):
    model = apps.get_model('review', 'BookReview')
    book = Book.objects.get(pk=pk)
    name = book.title.upper()
    review_list = model.objects.filter(title=name)
    review = next((x for x in review_list if x.title == name), None)
    context = {
        'instance': book,
        'review': review
    }
    if review_list.exists():
        return render(request, 'book/book_details.html', context)
    else:
        return render(request, 'book/book_details2.html', {'instance': book})


def payment(request, pk):

    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book/checkout.html', context)




