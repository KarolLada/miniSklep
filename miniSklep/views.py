from django.shortcuts import render, redirect, HttpResponse
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
                return redirect("sklep") 
            else:
                HttpResponse("Błędne dane logowania")
        except Users.DoesNotExist:
            HttpResponse("Błędne dane logowania")

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
    if request.method == "POST":
        if "usun" in request.POST:
            product_id = request.POST["usun"].split("|")
            product_name = product_id[0]
            product_price = int(product_id[1]) 
            
            try:
                usunProduct = Products.objects.get(name=product_name, price=product_price)
                usunProduct.delete()
                return redirect("products")
            except Products.DoesNotExist:
                return HttpResponse("Nie znaleziono produktu")
            
        if "edycja" in request.POST:
            product_id = request.POST["edycja"].split("|")
            product_name = product_id[0]
            product_price = int(product_id[1])  
            return redirect("edit", product_name=product_name, product_price=product_price) 
        
        if "usunAll" in request.POST:
            Products.objects.all().delete()
            return redirect("products")

    products = Products.objects.all()
    return render(request, "products.html", {"Products": products})

def edit(request, product_name, product_price):
    try:
        product = Products.objects.get(name=product_name, price=product_price)
    except Products.DoesNotExist:
        return HttpResponse("Nie znaleziono produktu")

    if request.method == "POST":
        new_name = request.POST.get("name")
        new_price = request.POST.get("price")

        if new_name and new_price:
            product.name = new_name
            product.price = int(new_price) 
            product.save()
            return redirect('products')  

    return render(request, 'edit.html', {'product': product})