from django.shortcuts import render,redirect
from seller.models import *
from django.contrib import messages
from django.http import JsonResponse
from site_admin.models import *
from buyer.models import *
import datetime
def seller_register(request):
    return render(request,'seller_registration.html')
def seller_registeraction(request):
    name = request.POST['name']
    gender = request.POST['gender']
    age = request.POST['age']
    address = request.POST['address']
    place = request.POST['place']
    phone = request.POST['phone']
    username = request.POST['username']
    password = request.POST['password']
    if len(request.FILES)>0:
        img = request.FILES['images']
    else:
        img ="no file"
    seller = seller_tb(Name=name,Gender=gender,Age=age,Addresss=address,Place=place,Phone=phone,username=username,password=password,image=img)
    seller.save()
    messages.add_message(request,messages.INFO,"Registration succesfull")
    return redirect('seller_register')
def getuser(request):
    user = request.GET['us']
    data = seller_tb.objects.filter(username=user)
    if len(data)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})
def sellerhome(request):
    return render(request,"sellerhome.html")
def addproducts(request):
    category = category_tb.objects.all()
    return render(request,"addproducts.html",{'cat':category}) 
def addproductAction(request):
    seller_id = request.session['sellerid']
    name = request.POST['name']
    price = request.POST['price']
    stock = request.POST['stock']
    details = request.POST['details']
    category = request.POST['category']
    if len(request.FILES)>0:
        img = request.FILES['image']
    else:
        img = "no file"
    products = product_tb(Name=name,Price=price,Stock=stock,Details=details,Image=img,category_id_id=category,seller_id_id=seller_id)
    products.save()
    return render(request,"sellerhome.html")
def viewproducts(request):
    seller_id =request.session['sellerid']
    products = product_tb.objects.filter(seller_id=seller_id)
    return render(request,"viewproducts.html",{'prod':products})
def editproducts(request,id):
    category = category_tb.objects.all()
    products = product_tb.objects.filter(id=id)
    return render(request,"editproducts.html",{'edit':products,'cat':category})
def editproductsAction(request):
    id = request.POST['id']
    product = product_tb.objects.filter(id=id)
    name = request.POST['name']
    price = request.POST['price']
    stock = request.POST['stock']
    details = request.POST['details']
    category = request.POST['category']
    if len(request.FILES)>0:
        img = request.FILES['image']
    else:
        img = product[0].Image
    products = product_tb.objects.filter(id=id).update(Name=name,Price=price,Stock=stock,Details=details,category_id_id=category)
    image_upload=product_tb.objects.get(id=id)
    image_upload.Image = img
    image_upload.save()
    return render(request,"viewproducts.html")
def deleteproducts(request,id):
    products = product_tb.objects.filter(id=id).delete()
    return render(request,"viewproducts.html")
def viewprofileseller(request):
    seller_id = request.session['sellerid']
    seller_profile = seller_tb.objects.filter(id=seller_id)
    return render(request,"viewprofileseller.html",{'prof_sell':seller_profile})
def editprofileseller(request):
    seller_id = request.session['sellerid']
    seller_profile = seller_tb.objects.filter(id=seller_id)
    id = request.POST['id']
    name = request.POST['name']
    gender = request.POST['gender']
    age = request.POST['age']
    address = request.POST['address']
    place = request.POST['place']
    phone = request.POST['phone']
    username = request.POST['username']
    if len(request.FILES)>0:
        img = request.FILES['image']
    else:
        img = seller_profile[0].image
    seller_profile = seller_tb.objects.filter(id=seller_id).update(Name=name,Gender=gender,Age=age,Addresss=address,Place=place,Phone=phone,username=username)
    Image_upload=seller_tb.objects.get(id=seller_id)
    Image_upload.image =img
    Image_upload.save()
    return redirect('viewprofileseller')
def vieworders(request):
    seller_id = request.session['sellerid']
    products = product_tb.objects.filter(seller_id_id=seller_id)
    ordersview = orderItems_tb.objects.filter(Product_id_id__in = products)
    return render(request,"vieworders.html",{'vieworder': ordersview})
def vieworderDetails(request,id):
    orders = orderItems_tb.objects.filter(Order_Id_id=id)
    return render(request,"vieworderDetails.html",{"order":orders})
def sellerapproval(request,id):
    approve = order_tb.objects.filter(id=id).update(Status="approved")
    messages.add_message(request,messages.INFO,"Approved")   
    return redirect('vieworders')
def sellerrejection(request,id):
    reject = order_tb.objects.filter(id=id).update(Status="reject")
    messages.add_message(request,messages.INFO,"Rejected")
    return redirect('vieworders')
def cancelorder(request,id):
    order_items = orderItems_tb.objects.filter(Order_Id_id = id)
    for i in order_items:
        product = i.Product_id_id
        print(product)
        products = product_tb.objects.get(id=product)
        stock = products.Stock
        quantity = i.Quantity
        stocks = stock+quantity
        change_stock = product_tb.objects.filter(id=product).update(Stock = stocks)
        print(stock)
        print(stocks)
    cancel = order_tb.objects.filter(id=id).update(Status="cancelled")
    messages.add_message(request,messages.INFO,"Cancelled")
    return redirect('vieworders')
def ordertracking(request,id):
    ordertrack = order_tb.objects.filter(id=id)
    return render(request,"ordertracking.html",{'track':ordertrack})
def ordertrackingAction(request):
    order_id = request.POST['order_id']
    orderdate = datetime.date.today()
    ordertime = datetime.datetime.now().strftime("%H:%M")
    details = request.POST['details']
    ordertracking = ordertracking_tb(Order_id_id=order_id,Orderdate=orderdate,Ordertime=ordertime,Details=details)
    ordertracking.save()
    return redirect('vieworders')
def sellerchangepassword(request):
    return render(request,"sellerchangepassword.html")
def sellerpasswordAction(request):
    seller_id = request.session['sellerid']
    seller = seller_tb.objects.filter(id=seller_id)
    for i in seller:
        password = i.password
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    if password == oldpassword:
        if newpassword == confirmpassword:
            changepassword = seller_tb.objects.filter(id=seller_id).update(password=confirmpassword)
            messages.add_message(request,messages.INFO,"Password updated")
        else:
            messages.add_message(request,messages.INFO,"Password mismatch")
    else:
        messages.add_message(request,messages.INFO,"Incorrect password")
    return redirect("sellerhome")
def logout(request):
    request.session.flush()
    return redirect('login')



    




  


# Create your views here.

