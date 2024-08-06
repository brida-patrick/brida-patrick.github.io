from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Book,Author
from .forms import BookModel
from datetime import datetime


def heure(request):
    now = datetime.now()
    contex = {'heure':now,}
    return render(request,'mnappli/heure.html',contex)





def index(request):
    contex = {'books':Book.objects.all()}
    return render(request,"mnappli/index.html",contex)
    #if request.method == 'POST':
        #form = someForm(request.POST)

        #if form.is_valid():
            #return redirect("mnappli:index")
        
    #else:
            #form = someForm()
    #contex = {'form' : form}
    #return render(request,"mnappli/index.html",contex)
    

   




    

@permission_required('mnappli.view_book')
def show (request,book_id):
    contex={"book": get_object_or_404(Book,pk=book_id)}
    return render(request,"mnappli/show.html",contex)



def add(request):
    if request.method == "POST":
        form = BookModel(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("mnappli:index")

    else:
        form= BookModel()
    contex= {"form":form}
    return render(request,"mnappli/ajout-livre.html",contex)
    

def edith(request,book_id):
    book = Book.objects.get(pk = book_id)
    if request.method == "POST":
        form= BookModel(request.POST, instance = book )
        if form.is_valid():
            form.save()
            return redirect("mnappli:index")
    else:
        form = BookModel(instance= book )
    contex= {"form":form}

    return render(request,"mnappli/modifier.html",contex)

   
def remove(request,book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect("mnappli:index")

    
    


