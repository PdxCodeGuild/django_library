from django.shortcuts import render, get_object_or_404, redirect

from books.models import Book, Transaction

def index(request):
    books = Book.objects.all()

    return render(request, 'books/index.html', {'books': books})

def checked_out(request):
    books = Book.objects.filter(checked_out=True)

    return render(request, 'books/index.html', {'books': books})

def checked_in(request):
    books = Book.objects.filter(checked_out=False)

    return render(request, 'books/index.html', {'books': books})

def checkout(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)

        if not book.checked_out:
            transaction = Transaction.objects.create(book=book)
            book.checked_out = True
            book.save()

            return redirect('books:index')

def checkin(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        
        if book.checked_out:
            transaction = Transaction.objects.create(book=book)
            book.checked_out = False 
            book.save()

            return redirect('books:index')