from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"] 


        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            
            return redirect("mnappli:index")
        else:
            messages.info(request,"mot de passe ou indentifiant incorrect")
    form = AuthenticationForm()
    contex = {'form':form}
    return render(request,"account/login.html",contex)


def logout_user(request):
    logout(request)
    return redirect("account:login")

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("account:login")


    else:
        form = UserCreationForm()

    return render(request,"account/register.html",{'form':form})
    
            


