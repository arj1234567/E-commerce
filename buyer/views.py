
from django.shortcuts import render, redirect
from buyer.models import *
from seller.models import * 
from django.contrib import messages
import datetime
def userhome(request):
    return render(request,'userhome.html')

def viewprofile(request):

    profile_id = request.session['userid']
    profile = Buyer_tb.objects.filter(id=profile_id)
    return render(request, 'viewprofile.html', {'prof': profile})

def editprofile(request):
    profile_id = request.session['userid']
    user = Buyer_tb.objects.filter(id=profile_id)
    id =request.POST['id']
    name = request.POST['name']
    age = request.POST['age']
    phone = request.POST['phone']
    address = request.POST['address']
    place = request.POST['place']
    gender = request.POST['gender']
    username = request.POST['username']
    user = Buyer_tb.objects.filter(id=id).update(Name =name,Gender =gender,Age=age,Addresss =address,Place=place,Phone=phone,username=username)
    return redirect('login')
def viewproductsbuyer(request):
    view_products = product_tb.objects.all()
    return render(request,"viewproductsbuyer.html",{'view_prod':view_products})
def add_to_cart(request,id):
    products = product_tb.objects.filter(id=id)
    return render(request,"add_to_cart.html",{'cart':products})
def addtocartAction(request):
    buyer_id = request.session['userid']
    quantity = request.POST['quantity']
    total = request.POST['total']
    product_id = request.POST['product_id']
    stock = request.POST['stock']
    print(stock)
    print(quantity)
    if int(quantity)>int(stock):
        messages.add_message(request,messages.INFO,"Out of Stock")
    else:
        carts = cart_tb(Quantity=quantity,Total=total,Buyer_id_id=buyer_id,Product_id_id=product_id)
        carts.save()
    return redirect('viewproductsbuyer')
def mycarts(request):
    buyer_id = request.session['userid']
    mycarts = cart_tb.objects.filter( Buyer_id_id=buyer_id)
    Grandtotal = 0
    for j in mycarts:
        total = j.Total
        Grandtotal = Grandtotal + total
    return render(request,"mycarts.html",{"carts":mycarts,"sum":Grandtotal})
def deletemycarts(request,id):
    mycarts = cart_tb.objects.filter(id=id).delete()
    return redirect('mycarts')
def orderAction(request):
    name = request.POST['name']
    address = request.POST['address']
    phone = request.POST['phone']
    buyer_id=request.session['userid']
    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M")
    grandtotal = request.POST['grandtotal']
    orders = order_tb(Name=name,Address=address,Phone=phone,Buyer_id_id=buyer_id,Orderdate = date,Ordertime=time,Grandtotal=grandtotal)
    orders.save()
    order_id = orders.id
    mycarts = cart_tb.objects.filter( Buyer_id_id=buyer_id)
    for i in mycarts:
        product_id = i.Product_id_id
        quantity=i.Quantity
        product = product_tb.objects.get(id=product_id)
        price=product.Price
        stock = product.Stock
        stocks = stock-quantity
        product_stock = product_tb.objects.filter(id=product_id).update(Stock=stocks)
        orderitems=orderItems_tb(Quantity=quantity,Price=price,Buyer_id_id=buyer_id,Order_Id_id=order_id,Product_id_id=product_id)
        orderitems.save()
        cart_delete = cart_tb.objects.filter(id=i.id).delete()
    return redirect('payment',orders.id)
def payment(request,id):
    order = order_tb.objects.filter(id=id)
    return render(request,"payment.html",{'grand':order})
def paymentAction(request):
    buyer_id = request.session["userid"]
    order_id = request.POST['order_id']
    name_card = request.POST['name_card']
    card_number = request.POST['card_number']
    exp_date = request.POST['exp_date']
    cvv = request.POST['cvv']
    payments = payment_tb(Name_on_card = name_card,Card_number =card_number,Expiry_date = exp_date,Cvv=cvv,Buyer_id_id=buyer_id,order_id_id=order_id)
    payments.save()
    return redirect('viewproductsbuyer')
def myorders(request):
    buyer_id = request.session['userid']
    myorders = order_tb.objects.filter(Buyer_id_id=buyer_id)
    return render(request,"myorders.html",{'orders': myorders})
def orderDetails(request,id):
    orderdetails = orderItems_tb.objects.filter(Order_Id_id = id)
    return render(request,"orderDetails.html",{'details':orderdetails})
def buyercancelorder(request,id):
    buyercancel = order_tb.objects.filter(id=id).update(Status="cancelled")
    messages.add_message(request,messages.INFO,"Cancelled")
    return redirect('myorders')
def viewtrack(request,id):
    viewtracks = ordertracking_tb.objects.filter(Order_id_id=id)
    return render(request,"viewtrack.html",{'viewtrack':viewtracks})
def changepassword(request):
    return render(request,"changepassword.html")
def changepasswordAction(request):
    buyer_id = request.session['userid']
    buyer = Buyer_tb.objects.filter(id=buyer_id)
    for i in buyer:
        password = i.password
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    if password == oldpassword:
        if newpassword == confirmpassword:
            changepassword = Buyer_tb.objects.filter(id=buyer_id).update(password=confirmpassword)
            messages.add_message(request,messages.INFO,"Password updated")
        else:
            messages.add_message(request,messages.INFO,"Password Mismatch")
    else:
        messages.add_message(request,messages.INFO,"Incorrect Password")
    return redirect('userhome')
def forgetpassword(request):
    return render(request,"forgetpassword.html")
def forgetpassword1(request):
    name1 = request.POST['name1']
    buyer = Buyer_tb.objects.filter(username = name1)
    seller = seller_tb.objects.filter(username=name1)
    if buyer.count()>0:
        request.session['username'] = buyer[0].username
        return render(request,"forgetpassword1.html")
    elif seller.count()>0:
        request.session['username'] = seller[0].username
        return render(request,"forgetpassword1.html")
    else:
        messages.add_message(request,messages.INFO,"Invalid Username")
        return redirect('login')
def newpassword(request):
    name2 = request.POST['name2']
    age1 = request.POST['age1']
    phone1 = request.POST['phone1']
    buyer = Buyer_tb.objects.filter(Name=name2,Age=age1,Phone=phone1)
    seller = seller_tb.objects.filter(Name=name2,Age=age1,Phone=phone1 )
    if buyer.count()>0:
        return render(request,"newpassword.html")
    elif seller.count()>0:
        return render(request,"newpassword.html")
    else:
        messages.add_message(request,messages.INFO,"Invalid data")
        return redirect('login')
def newpasswordAction(request):
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    username = request.session['username']
    buyer = Buyer_tb.objects.filter(username=username)
    for i in buyer:
        buyer_id = i.id
    seller = seller_tb.objects.filter(username = username)
    for j in seller:
        seller_id = j.id
    if newpassword == confirmpassword:
        if buyer.count()>0:
            passwordchange = Buyer_tb.objects.filter(id=buyer_id).update(password=confirmpassword)
        else:
            passwordchange1  = seller_tb.objects.filter(id = seller_id).update(password = confirmpassword)
    else:
        messages.add_message(request,messages.INFO,"Password mismatch")
    return redirect('login')
def product_search(request):
    search=request.POST['search']
    product = product_tb.objects.filter(Name__istartswith=search) or product_tb.objects.filter(Price=search)
    return render(request,"viewproductsbuyer.html",{'view_prod':product})
    # product_price =product_tb.objects.filter(Price=search)
    # if product:
    #     return render(request,"viewproductsbuyer.html",{'view_prod':product})
    # elif product_price:
    #     return render(request,"viewproductsbuyer.html",{'view_prod':product_price})
    # else:
    #     return redirect('viewproductsbuyer')
def logout(request):
    request.session.flush()
    return redirect('login')


    


    





  



