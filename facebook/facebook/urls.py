"""facebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from fb import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index',views.index,name='index'),
    url(r'^SignUp', views.SignUp, name='SignUp'),
    url(r'^Login', views.Login, name='Login'),
    url(r'^Welcome', views.Welcome, name='Welcome'),
    url(r'^SendRequest', views.SendRequest, name='SendRequest'),
    url(r'^Accept', views.Accept, name='Accept'),
    url(r'^Reject', views.Reject, name='Reject'),
    url(r'^savepost', views.savepost, name='savepost'),
    url(r'^Disp', views.Disp, name='Disp'),
    url(r'^Exp', views.Exp, name='Exp'),
    url(r'^ajaxpage1', views.ajaxpage1, name='ajaxpage1'),
    url(r'^ajaxpage2', views.ajaxpage2, name='ajaxpage2'),
    url(r'^AJAX1', views.AJAX1, name='AJAX1'),
    url(r'^AJAX2', views.AJAX2, name='AJAX2'),
    url(r'^uploadpic', views.uploadpic, name='uploadpic'),
]
