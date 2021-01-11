from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author

# Create your views here.
def index(request):
	return render(request,'books/index.html')
	
def list_view(request):
	list_all_books = Book.objects.all()
	
	return render(request, 'books/list.html', {'books': list_all_books})
	
def detail_view(request, book_id):
	book = Book.objects.get(id=book_id)
	shelf_info = book.get_shelf_info()
	author = book.author
	if author.name != 'Inconnu':
		context = {
				'book': book,
				'row': shelf_info[0],
				'shelf': shelf_info[1],
				'first_book': author.first_book,
				'author_name':author.name,
				'author_phone': author.phone_number,
				'author_mail': author.mail,
		}
	else:
		context = {
				'book': book,
				'row': shelf_info[0],
				'shelf': shelf_info[1],
		}
	# context = {'book':book}
	
	return render(request, 'books/detail.html', context)
	
def lent_view(request):
	# Récupérer les livres NON empruntés (donc disponibles)
	# books = Book.objects.filter(lent_to = None)
	
	# Récupérer les livres empruntés (dont le champ lent_to n'est PAS vide)
	books = Book.objects.exclude(lent_to=None)
	
	# Récupérer les livres ECRITS PAR ROWLING empruntés (dont le champ lent_to n'est PAS vide)
	rowling = Author.objects.get(name='Rowling')
	books = Book.objects.exclude(lent_to=None).filter(author = rowling)
	# books = Book.objects.filter(author = rowling).exclude(lent_to=None)
	
	return render(request, 'books/lent_books.html', {'books':books})