from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pricing
from .models import Items,Ditems,ArchItems,AgriItems
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.mail import send_mail
# Create your views here.
def Home(request):
    price =Pricing.objects.all()

    return render(request,'Home.html',{'price':price})

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/Bcategory')

        else:

            messages.error(request,'Invalid Username ')
            return redirect('/login')

    else :
        return render(request,'login.html')


def signup(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/signup')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/signup')

            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('/login')
        
        else:
            messages.info(request,'Password Not Matching')
            return redirect('/signup')
        return redirect("/login")

    
    else:

        return render(request,'signup.html')

def items(request):
    item =Items.objects.all()

    return render(request,'items.html',{'Item' : item})

def ditems(request):
    item =Ditems.objects.all()

    return render(request,'Ditems.html',{'Item' : item,'value': True})


def agriItems(request):
    item =AgriItems.objects.all()

    return render(request,'AgriItems.html',{'Item' : item})

def Selling(request):
    return render(request,'Selling.html')

def Dselling(request):
    return render(request,'Dselling.html')

def AgriSelling(request):
    return render(request,'AgriSelling.html')

def ArchSelling(request):
    return render(request,'ArchSelling.html')

def archItems(request):
    item =ArchItems.objects.all()

    return render(request,'ArchItems.html',{'Item' : item})

def Bcategory(request):
    return render(request,'Bcategory.html')

@login_required(login_url='/login')
def Scategory(request):
    return render(request,'Scategory.html')

class  sell(CreateView):
    model= Items
    template_name = 'sell.html'
    fields = '__all__'

class  dsell(CreateView):
    model= Ditems
    template_name = 'sell.html'
    fields = '__all__'

class  archsell(CreateView):
    model= ArchItems
    template_name = 'sell.html'
    fields = '__all__'


class  agrisell(CreateView):
    model= AgriItems
    template_name = 'sell.html'
    fields = '__all__'


def aboutus(request):
    return render(request,'aboutus.html')


def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message =request.POST['message']



        send_mail(
            name,
            message,
            email,
            ['anilthapa1939@gmail.com'],
            fail_silently= False
        )
        return render(request,'contactus.html',{'name':name})


    else :
        return render(request,'contactus.html')

def seller(request):
    return render(request,'seller.html')
