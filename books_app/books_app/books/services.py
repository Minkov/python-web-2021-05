from books_app.books.models import Book


class BooksService:
    def get_by_state(self, state):
        books = []
        if state == 'all':
            return Book.objects.all()
            pass
