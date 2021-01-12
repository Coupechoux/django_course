from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Book, Author, Person
from .forms import PersonForm

# Create your views here.
def index(request):
	print(dir(request))
	print(request.get_full_path())
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
	
def add_person(request):
	# Si le client a envoyé des données
	if request.method == 'POST':
		# print(request.POST)
		
		# Créer un objet formulaire, rempli avec les données envoyées par le client
		form = PersonForm(request.POST)
		
		# Vérifier les données et remplir l'attribut 'cleaned_data' si les données sont correctes
		if form.is_valid():
			data = form.cleaned_data
			print('Données correctes :', data)
			
			# Traiter les données
			# Je vérifie que le 'name' n'existe pas déjà dans la base de données
			r = Person.objects.filter(name=data['name'])
			if len(r) == 0:
				p = Person(name=data['name'], mail=data['mail'], phone_number=data['phone_number'])
				p.save()
			else:
				p = r[0]
				p.mail = data['mail']
				p.phone_number = data['phone_number']
				p.save()
			
			# Je redirige le client vers une page, pour éviter de renvoyer les données en actualisant
			# reverse est l'équivalent du tag {% url %} : cette fonction permet de convertir un nom en url (en utilisant les 'name' du fichier urls.py
			return HttpResponseRedirect(reverse('add_person'))
			
		# else:
			# Sinon (les données ne sont pas correctes), je ne fais rien. L'objet form contient les erreurs.
			# pass
	else: # Si le client demande un formulaire vierge
		form = PersonForm()

	# Ici, j'ai un objet form qui contient les données/erreurs s'il y en a, ou qui est vierge sinon.

	return render(request, 'books/add_person.html', {'form':form})