from django.shortcuts import render,redirect
from . models import Books, Authors

# Create your views here.
def index(request):
    context = {
        "bookList" : Books.objects.all().order_by('id'),
    }

    return render(request,'books_authors/index.html',context)

def add_book(request):
    Books.objects.create(title=request.POST['title'], description= request.POST['desc'])
    return redirect('/')

def display_book(request,id):

    if request.method == "GET" :

        book = Books.objects.get(id=id)
        context = {
            "this_book" : Books.objects.get(id=id),
            "authors" : book.authors.all(),
            "all_authors" : Authors.objects.all(),
        }
        return render(request,'books_authors/display.html', context)

    if request.method == "POST":
        book = Books.objects.get(id=id)
        author = Authors.objects.get(id=request.POST['id_author']) 
        book.authors.add(author)
        return redirect(f'/display_book/{id}')
