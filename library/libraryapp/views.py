from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Book, Author, Availability
# Create your views here.

def index(request):
    book_list = Availability.objects.all()
    context = {'books':book_list}
    return render(request, 'libraryapp/index.html', context)

# @login_required
def add_book(request):
    if request.method == "POST":
        new_author_name = request.POST['author_name']
        new_title = request.POST['title']
        new_publish_date = request.POST['publish_date']
        if not Author.objects.filter(author_name=new_author_name).exists():
            create_new_author = Author(author_name=new_author_name)
            create_new_author.save()
        author_id = Author.objects.filter(author_name=new_author_name)[0]
        new_book = Book(title=new_title, publish_date=new_publish_date, author=author_id)
        new_book.save()
        new_availability = Availability(book=new_book)
        new_availability.save()
    return HttpResponseRedirect(reverse('libraryapp:index'))

# @login_required
def delete_book(request, pk):
    target_book = get_object_or_404(Availability, pk=pk)
    target_book.delete()
    return HttpResponseRedirect(reverse('libraryapp:index'))

# @login_required
def checkout_book(request, pk):
    target_book = get_object_or_404(Availability, pk=pk)
    target_book.user = request.user.username
    if target_book.checkout:
        target_book.user = 'Currently Available'
    target_book.checkout = (not target_book.checkout)
    target_book.save()
    return HttpResponseRedirect(reverse('libraryapp:index'))

# @login_required
def return_book(request, pk):
    return HttpResponse('Book returned')
