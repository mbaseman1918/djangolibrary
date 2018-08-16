from django.urls import path
from . import views

app_name = 'libraryapp' # for namespacing
urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('checkout_book/<int:pk>/', views.checkout_book, name='checkout_book'),
    path('return_book/<int:pk>', views.return_book, name='return_book'),
    path('', views.index, name='index'),
]
