from django.shortcuts import render, redirect
from .models import Products, Users
from django.contrib.auth.hashers import make_password, check_password

def sklep(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
  
        product = Products(
            name=name,
            price=price,
        )

        product.save()

    return render(request, "sklep.html")

def sklepLogin(request):
    if request.method == "POST":
        login = request.POST.get("login")
        passw = request.POST.get("passw")

        try:
            user = Users.objects.get(login=login)

            if check_password(passw, user.passw):
                return redirect('sklep') 
            else:
                return render(request, "sklepLogin.html", {"error": "Błędne dane logowania"})
        except Users.DoesNotExist:
            return render(request, "sklepLogin.html", {"error": "Błędne dane logowania"})

    return render(request, "sklepLogin.html")

def register(request):
    if request.method == "POST":
        login = request.POST.get("login")
        passw = request.POST.get("passw")
        
        hashPass = make_password(passw)
        
        user = Users(
            login=login,
            passw=hashPass,
        )
        user.save()

    return render(request, "register.html")


def products(request):
    products = Products.objects.all()
    return render(request, "products.html", {"Products": products})