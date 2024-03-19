from django.shortcuts import render,redirect
from site_admin.models import *
from buyer.models import *
from seller.models import *
from django.contrib import messages
from django.http import JsonResponse
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username = request.POST['username']
    password = request.POST['password']
    user = Buyer_tb.objects.filter(username= username,password =password)
    user1 = admin_tb.objects.filter(username= username,password =password)
    seller = seller_tb.objects.filter(username=username,password=password)
    if user.count()>0:
        messages.add_message(request,messages.INFO,'Login Succesfull...')
        request.session['userid'] = user[0].id
        return render(request,"userhome.html")
    elif user1.count()>0:
        messages.add_message(request,messages.INFO,"Login Succesfull")
        request.session['user1id']=user1[0].id
        return render(request,"adminhome.html")
    elif seller.count()>0:
        if seller[0].status == "approved":
            messages.add_message(request,messages.INFO,"Login Succesfull")
            request.session['sellerid']=seller[0].id
            return render(request,"sellerhome.html")
        else:
            messages.add_message(request,messages.INFO,'Please wait for approval')
            return redirect('login')
    else:
        messages.add_message(request,messages.INFO,'Login Failed...')
        return redirect('login')
def register(request):
    return render(request,'register.html')
def registerAction(request):
    name = request.POST['name']
    gender = request.POST['gender']
    age = request.POST['age']
    address = request.POST['address']
    place = request.POST['place']
    phone = request.POST['phone']
    username = request.POST['username']
    password = request.POST['password']
    user = Buyer_tb(Name=name,Gender=gender,Age=age,Addresss=address,Place=place,Phone=phone,username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,'Registration succesfull....')
    return redirect('register')
def addcategory(request):
    return render(request,'addcategory.html')
def categoryAction(request):
    name = request.POST['name']
    cat = category_tb(name=name)
    cat.save()
    return render(request,'addcategory.html')
def viewcategory(request):
    category = category_tb.objects.all()
    return render(request,'viewcategory.html',{'cat':category})
def getuser(request):
    user = request.GET['us']
    data = Buyer_tb.objects.filter(username=user)
    if len(data)>0:
        msg="exist"
    else:
        msg ="not exist"
    return  JsonResponse({'valid':msg})
def viewseller(request):
    seller = seller_tb.objects.all()
    return render(request,'viewseller.html',{'sell':seller})
def approved(request,id):
    seller_approval = seller_tb.objects.filter(id=id).update(status="approved")
    messages.add_message(request,messages.INFO,"Approved")
    return render(request,'approved.html')
def rejected(request,id):
    seller_rejected = seller_tb.objects.filter(id=id).update(status="rejected")
    messages.add_message(request,messages.INFO,"Rejected")
    return render(request,"rejected.html")

    
    


# Create your views here.
