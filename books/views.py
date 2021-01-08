from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
	return render(request,'books/index.html')
	
def list_view(request):
	b = Book.objects.get(title='Harry Potter 1')
	
	context_dict = {'book':b}
	return render(request, 'books/list.html', context_dict)
	
def detail_view(request, book_id):
	return HttpResponse(f"Détail du livre {book_id}.")
	
def lent_view(request):
	return HttpResponse('Ceci est la liste des livres indisponibles.')