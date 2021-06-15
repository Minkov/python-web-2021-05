from django.shortcuts import render, redirect

from books_app.books.forms import BookForm, AuthorForm, StateFilterForm
from books_app.books.models import Book
from books_app.books.services import BooksService


def show_book_form(request, book_form, author_form, template_name):
    context = {
        'book_form': book_form,
        'author_form': author_form,
    }

    return render(request, template_name, context)


def save_book_from_form(request, book_form, author_form, template_name):
    if book_form.is_valid() and author_form.is_valid():
        author = author_form.save()
        book = book_form.save(commit=False)
        book.author = author
        book.save()
        return redirect('index')

    return show_book_form(request, book_form, author_form, template_name)


def index(request):
    service = BooksService()
    filter_form = StateFilterForm(request.GET)
    filter_form.is_valid()
    state = filter_form.cleaned_data['state']

    context = {
        'filter_form': filter_form,
        'books': service.get_by_state(state),
    }

    return render(request, 'index.html', context)


def create_book(request):
    if request.method == 'GET':
        book_form = BookForm()
        author_form = AuthorForm()
        return show_book_form(request, book_form, author_form, 'create.html')
    else:
        book_form = BookForm(request.POST)
        author_form = AuthorForm(request.POST)

        return save_book_from_form(request, book_form, author_form, 'create.html')


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
        return show_book_form(request, form, 'edit.html')
    else:
        form = BookForm(
            request.POST,
            instance=book,
        )
        return save_book_from_form(request, form, 'edit.html')
