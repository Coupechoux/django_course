from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books_index'),
	path('list/', views.list_view, name='books_list'),
	path('detail/<int:book_id>', views.detail_view, name='books_detail'),
	path('lent/', views.lent_view, name='lent_books'),
	path('add/person/', views.add_person, name='add_person'),
	path('add/book/', views.add_book, name='add_book'),
]
