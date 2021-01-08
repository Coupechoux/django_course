from django.contrib import admin
from .models import Book, Person, Author, AuthorsGroup

# Register your models here.
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'shelf', 'author', 'lent_to')
	ordering = ('shelf','title')
	list_filter = ('shelf',)
	search_fields = ('title','shelf')
	# fields = ('title',)

admin.site.register(Book, BookAdmin)

# On peut faire pareil avec Person et Author, à titre d'exercice ! :)
admin.site.register(Person)
admin.site.register(Author)
admin.site.register(AuthorsGroup)