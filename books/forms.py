from django import forms
from django.core.exceptions import ValidationError
from .models import Author
from django.core.validators import MinLengthValidator

def phone_validator(s):
	# if len(s) != 10 or not s.isdigit() or s[0] != '0':
		# raise ValidationError('Mauvais format de téléphone')
	if len(s) != 10:
		raise ValidationError('Le numéro doit contenir 10 chiffres.')
	if not s.isdigit():
		raise ValidationError('Le numéro ne doit contenir QUE des chiffres.')
	if s[0] != '0':
		raise ValidationError("Le numéro doit commencer par un '0'.")

class PersonForm(forms.Form):
	name = forms.CharField(max_length = 30, label='Nom ')
	# mail = forms.CharField(max_length = 50, label='E-mail ', required=False)
	mail = forms.EmailField(label='E-mail ', required=False)
	
	phone_number = forms.CharField(max_length = 10, label='Téléphone ', required=False, validators=[phone_validator])
	# Format spécial pour le numéro de téléphone :
	# - Il doit être exactement de taille 10
	# - Il ne doit contenir que des chiffres
	# - Il doit commencer par '0'
	
def shelf_validator(s):
	if len(s) != 5 or s[0] != 'E' or not s[1:].isdigit():
		raise ValidationError("Mauvais format d'étagère")
	
class BookForm(forms.Form):
	title = forms.CharField(max_length=200, label='Titre ')
	shelf = forms.CharField(max_length=5, label='Code étagère ', validators=[shelf_validator])
	author1 = forms.ModelChoiceField(queryset=Author.objects.exclude(name='Inconnu'), required=False, label="Auteur 1 ")
	author2 = forms.CharField(max_length=30, label="Auteur 2 ", validators=[MinLengthValidator(2)])