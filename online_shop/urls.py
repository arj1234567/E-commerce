"""
URL configuration for online_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site_admin import views as adminview
from buyer import views as buyerview 
from seller import views as sellerview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name= "index"),
    path('login/',adminview.login,name ="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('register/',adminview.register,name="register"),
    path('registerAction/',adminview.registerAction,name="registerAction"),
    path('sellerhome/',sellerview.sellerhome,name="sellerhome"),
    path('userhome/',buyerview.userhome,name="userhome"),
    path('addcategory/',adminview.addcategory,name="addcategory"),
    path('categoryAction/',adminview.categoryAction,name="categoryAction"),
    path('viewcategory/',adminview.viewcategory,name="viewcategory"),
    path('viewprofile/',buyerview.viewprofile,name="viewprofile"),
    path('editprofile/',buyerview.editprofile,name="editprofile"),
    path('seller_register/',sellerview.seller_register,name="seller_register"),
    path('seller_registeraction/',sellerview.seller_registeraction,name="seller_registeraction"),
    path('getuser/',sellerview.getuser,name="getuser"),
    path('getuser/',adminview.getuser,name="getuser"),
    path('viewseller/',adminview.viewseller,name="viewseller"),
    path('approved<int:id>/',adminview.approved,name="approved"),
    path('rejected<int:id>/',adminview.rejected,name="rejected"),
    path('addproducts/',sellerview.addproducts,name="addproducts"),
    path('addproductAction/',sellerview.addproductAction,name="addproductAction"),
    path('viewproducts/',sellerview.viewproducts,name="viewproducts"),
    path('editproducts<int:id>/',sellerview.editproducts,name="editproducts"),
    path('editproductsAction',sellerview.editproductsAction,name="editproductsAction"),
    path('deleteproducts<int:id>/',sellerview.deleteproducts,name="deleteproducts"),
    path('viewprofileseller/', sellerview.viewprofileseller,name="viewprofileseller"),
    path('editprofileseller/',sellerview.editprofileseller,name="editprofileseller"),
    path('viewproductsbuyer/',buyerview.viewproductsbuyer,name="viewproductsbuyer"),
    path('add_to_cart<int:id>/',buyerview.add_to_cart,name="add_to_cart"),
    path('addtocartAction/',buyerview.addtocartAction,name="addtocartAction"),
    path('mycarts/',buyerview.mycarts,name="mycarts"),
    path('deletemycarts<int:id>/',buyerview.deletemycarts,name="deletemycarts"),
    path('orderAction/',buyerview.orderAction,name="orderAction"),
    path('payment<int:id>/',buyerview.payment,name="payment"),
    path('paymentAction/',buyerview.paymentAction,name="paymentAction"),
    path('myorders/',buyerview.myorders,name="myorders"),
    path('orderDetails<int:id>/',buyerview.orderDetails,name="orderDetails"),
    path('vieworders/',sellerview.vieworders,name="vieworders"),
    path('vieworderDetails<int:id>/',sellerview.vieworderDetails,name="vieworderDetails"),
    path('sellerapproval<int:id>/',sellerview.sellerapproval,name="sellerapproval"),
    path('sellerrejection<int:id>/',sellerview.sellerrejection,name="sellerrejection"),
    path('cancelorder<int:id>/',sellerview.cancelorder,name="cancelorder"),
    path('buyercancelorder<int:id>/',buyerview.buyercancelorder,name="buyercancelorder"),
    path('ordertracking<int:id>/',sellerview.ordertracking,name="ordertracking"),
    path('ordertrackingAction',sellerview.ordertrackingAction,name="ordertrackingAction"),
    path('viewtrack<int:id>/',buyerview.viewtrack,name="viewtrack"),
    path('changepassword/',buyerview.changepassword,name="changepassword"),
    path('changepasswordAction/',buyerview.changepasswordAction,name="changepasswordAction"),
    path('sellerchangepassword/',sellerview.sellerchangepassword,name="sellerchangepassword"),
    path('sellerpasswordAction/',sellerview.sellerpasswordAction,name="sellerpasswordAction"),
    path('forgetpassword/',buyerview.forgetpassword,name="forgetpassword"),
    path('forgetpassword1/',buyerview.forgetpassword1,name="forgetpassword1"),
    path('newpassword',buyerview.newpassword,name="newpassword"),
    path('newpasswordAction/',buyerview.newpasswordAction,name="newpasswordAction"),
    path('logout/',buyerview.logout,name="logout"),
    path('logout/',sellerview.logout,name="logout"),
    path('product_search/',buyerview.product_search,name="product_search"),
    
    


  
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
