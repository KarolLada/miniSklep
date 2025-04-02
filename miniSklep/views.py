from django.shortcuts import render, redirect
from .models import Products, Users

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
    if request.method == "GET":
        login = request.POST.get("login")
        passw = request.POST.get("passw")
  
        user = Users(
            login=login,
            passw=passw,
        )
        
    return render(request, "sklepLogin.html")

def register(request):
    if request.method == "POST":
        login = request.POST.get("login")
        passw = request.POST.get("passw")
  
        user = Users(
            login=login,
            passw=passw,
        )

        user.save()

    return render(request, "register.html")

def products(request):
    products = Products.objects.all()
    return render(request, "products.html", {"Products": products})