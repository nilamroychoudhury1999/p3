from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contacts,Article
from .import forms

# Create your views here.
def Base(request):
    return render(request,"home.html")

def Home(request):
    return render(request,"home.html")
    
def Contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("message")
        myquery = Contacts(name =name,email=email,message=msg)
        myquery.save()
        messages.info(request,"Thanks for contacting,we will get back to you soon")
        return redirect('/')
    return render(request,"contact.html")

def Article_detail(request,slug):
    article = Article.objects.get(id=slug)
    return render(request,'article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def Add_article(request):
    if request.method=="POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.info(request,"Thanks for Adding Article .")
            return redirect('/')
    else:
        form = forms.CreateArticle()
    return render(request,"create_article.html",{ 'form': form })


def Article_list(request):
    article = Article.objects.all().order_by('date')
    return render(request,'articles_list.html',{'articles':article})

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        myuser = authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"login Successfull")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,"login.html")

def SignUp(request):
    if request.method == "POST":
        username=request.POST.get('username')
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        print(firstname)
        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/accounts/signup/')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"UserName is Taken")
                return redirect('/accounts/signup/')
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/accounts/signup/')
        except Exception as identifier:
            pass
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/accounts/login/')
    return render(request,"signup.html")

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/accounts/login/')