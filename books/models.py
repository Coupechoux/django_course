from django.db import models


class Person(models.Model):
	name = models.CharField(max_length = 30)
	mail = models.CharField(max_length = 50, blank=True, null=True)
	phone_number = models.CharField(max_length = 10, blank=True, null=True)
	
	read_books = models.ManyToManyField('Book', related_name = 'readers')
	
	def __str__(self):
		return 'Personne : '+self.name

class Author(Person):
	
	
	def unknown_author():
		"""Returns the unknown default author, creating it if necessary"""
		# Ce qu'on a vu
		# return Author.objects.get(name='Inconnu').pk
		
		# Un petit peu plus propre (système de gestion d'exceptions)
		try:
			id = Author.objects.get(name='Inconnu').pk
		except Author.DoesNotExist as e:
			# Dans ce cas, je le crée
			unknown = Author(name='Inconnu')
			unknown.save()
			id = unknown.pk
		# except Author.MultipleObjectsReturned as e: <- je ne gère pas ce cas là, donc la fonction va transmettre l'erreur si elle survient
		return id
		
		# Encore mieux : voir get_or_create()
		# https://docs.djangoproject.com/en/3.1/ref/models/querysets/#get-or-create
			
		
	def __str__(self):
		return 'Auteur : '+self.name


class Book(models.Model):
	title = models.CharField(max_length = 200, default = 'Titre par défaut')
	shelf = models.CharField(max_length = 5, blank=True, null=True)
	
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=Author.unknown_author, related_name='get_all_books')
	
	lent_to = models.ForeignKey(Person, blank=True, null=True, on_delete=models.SET_NULL)
	
	# En exercice :
	def get_shelf_info(self):
		"""
		Returns a tuple containing the row number and the shelf number.
		For example, if b.shelf equals 'E0415', print(b.get_shelf_info()) will print ('04', '15').
		"""
		pass
	
	def __str__(self):
		return self.title

class AuthorsGroup(models.Model):
	name = models.CharField(max_length = 50)
	creation_date = models.IntegerField()
	still_alive = models.BooleanField(default = True)
	description = models.TextField()
	
	authors = models.ManyToManyField(Author, related_name='groups')
	
