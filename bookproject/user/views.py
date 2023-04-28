from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import AbstractUserForm
from django.apps import apps
from .forms import EditForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) is now changed to
        form = AbstractUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Here we are accessing username just to send a success message.
            username = form.cleaned_data['username']
            messages.success(request, f'{username} has created account successfully!')
            return redirect('books/')
    else:
        # If we don't try to "post" our form data it will return an empty form.
        form = AbstractUserForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def user_account(request):
    model = apps.get_model('book', 'Book')
    books = model.objects.filter(uploaded_by=request.user)
    context = {
        'books': books,
    }
    return render(request, 'user/account.html', context)


def edit_book(request, pk):
    model = apps.get_model('book', 'Book')
    book = model.objects.get(pk=pk)
    form = EditForm(instance=book)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('account/')
    return render(request, 'user/edit_form.html', {'form': form})


def delete_book(request, pk):
    model = apps.get_model('book', 'Book')
    book = model.objects.get(pk=pk)
    book.delete()
    title = book.title
    messages.success(request, f'{title} was deleted from the table.')
    return user_account(request)







