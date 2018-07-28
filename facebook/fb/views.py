from django.shortcuts import render, redirect
from django.http import HttpResponse
from fb.models import User
from fb.models import Friend
from fb.models import Wpost
from fb.models import Data
from fb.models import Player_Profile
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html")

def SignUp(request):
    u=User()
    u.email=request.GET.get("email")
    u.pwd = request.GET.get("pwd")
    u.name = request.GET.get("name")
    u.gender = request.GET.get("gender")
    u.save()
    return HttpResponse("Sign Up Successfull")

def Login(request):
    user=User.objects.filter(email=request.GET.get("email"),pwd=request.GET.get("pwd"))
    if user.exists()==True:
        request.session["email"]=request.GET.get("email")
        res=redirect("Welcome")
        return res
    else:
        return render(request,"index.html",{"error":"invalid id or password"})

def Welcome(request):
    friends=Friend.objects.filter(rec=request.session.get("email"),status=0)
    myfriends=GetFriends(request.session.get("email"))

    allfriends=myfriends
    allfriends.append(request.session.get("email"))
    w=Wpost.objects.all()
    myposts=[]
    pp = Player_Profile.objects.all()
    for ww in w:
        if allfriends.count(ww.sender)>0:
            myposts.append(ww.sender+"-"+ww.msg)

    return render(request,"welcomenew.html",{"fmsg":"","rlist":friends,"myfriends":myfriends,"msg":myposts,"users":pp})

def SendRequest(request):
    f=Friend()
    f.sender=request.session.get("email")
    f.rec=request.GET.get("rec")
    f.status=0
    f.save()
    res=redirect("Welcome")
    return res

def Accept(request):
    f=Friend.objects.get(id=request.GET.get("id"))
    f.status=1
    f.save()
    res = redirect("Welcome")
    return res

def Reject(request):
    f=Friend.objects.get(id=request.GET.get("id"))
    f.status=2
    f.save()
    res = redirect("Welcome")
    return res

def GetFriends(uid):
    f= Friend.objects.filter(Q(sender=uid) | Q(rec=uid),status=1)
    friends=[]
    for ff in f:
        if ff.sender==uid:
            friends.append(ff.rec)
        else:
            friends.append(ff.sender)
    return friends

def savepost(request):
    w=Wpost()
    w.sender=request.session.get("email")
    w.msg=request.GET.get("msg")
    w.save()
    res=redirect("Welcome")
    return res

def uploadpic(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            age = request.POST.get('age')
            pic = request.FILES.get('myfile')
            profile_obj = Player_Profile(profile_picture=pic, name=username, email=email, age=age).save()
        return redirect("Welcome")

def Exp(request):
    return render(request,"exp.html")


def Disp(request):
    f=User.objects.filter(name__startswith=request)
    s=""
    for u in f:
        s=s+u.name+"<br>"
    return HttpResponse(s)

def ajaxpage1(request):
    return render(request,"ajax1.html")


def ajaxpage2(request):
    return render(request,"ajax2.html")

def AJAX1(request):
    n=request.GET.get("name")
    users=User.objects.filter(name__startswith=n)
    s="<select size='10' onchange='disp1(this.value)'>"
    for u in users:
        s=s+"<option>"+u.name+"</option>"
    s=s+"</select>"
    return HttpResponse(s)


def AJAX2(request):
    n=request.GET.get("s")
    d=Data.objects.filter(state=n)
    s=""
    for dd in d:
        s=s+"<option>"+dd.city+"</option>"

    return HttpResponse(s)
















