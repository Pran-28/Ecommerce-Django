from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .constants import base_Url
import json
import string
import random
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def loginRender(request):
    print("****************** loginRender ******************")
    return render(request, "ecomstore/login.html", {'baseUrl': base_Url})


@csrf_exempt
def login(request):
    if request.method == "POST":
        json_response={}
        try:
            jsonData = request.POST.get('payload')
            print('jsondata====>', jsonData)
            
            parsedData = json.loads(jsonData)
            print('parsedData---->', parsedData)
            
            username = parsedData.get('username')
            print('username====>', username)
            
            email = parsedData.get('email')
            print('email====>', email)
            
            if len(username) > 0 and len(email) > 0:
                user = User.objects.filter(username=username).filter(email=email).values()
                print('user====>', user)
                
                if len(user) > 0 :
                    userid = user[0]['id']
                    username = user[0]['username']
                    first_name = user[0]['first_name']
                    last_name = user[0]['last_name']
                    email = user[0]['email']
                    print("Details --->",userid, username, first_name, last_name, email)
                    
                    char_set = string.ascii_uppercase + string.digits
                    session_key = ''.join(random.sample(char_set * 20,  20))
                    print("session_key===>", session_key)
                    
                    request.session["session_key"] = session_key
                    request.session["userid"] = userid
                    request.session["username"] = username
                    request.session["email"] = email
                    
                    json_response["status"] = True
                    json_response["message"] = "Login Successfull"
                    
                    return JsonResponse(json_response)
            else:
                json_response["status"] = False
                json_response["message"] = "Login Failed"      
                
                return JsonResponse(json_response)
                
        except Exception as e:
            print("error=--->", e)
            json_response["status"] = False
            json_response["message"] = "Something went wrong"
            return JsonResponse(json_response) 





@csrf_exempt
def logout(request):
    print("****************** logout ******************")
    if request.session.has_key('session_key'):
        del request.session['session_key']
        return redirect(base_Url)
    return redirect(base_Url)


def store(request):
    if request.session.has_key("session_key"):
        products = Product.objects.all()
        print('products===>', products)
        context = {'products':products}
        return render(request, "ecomstore/store.html", context)


def cart(request):
    if request.session.has_key("session_key"):
        userId = request.session.get('userid')
        print('userId====>', userId)
        
        username = request.session.get('username')
        print('username---->', username)
        
        email = request.session.get('email')
        print('email====>', email)
        
        customer = Customer.objects.filter(email=email).values()
        print("customer---->", customer)
        
        orders = Order.objects.filter(customer=customer).values()
        items = orders
        print("items--->", items)
    
        context = {'items' :  items}
        return render(request, "ecomstore/cart.html", context)


def checkout(request):
    context = {}
    return render(request, "ecomstore/checkout.html", context)
