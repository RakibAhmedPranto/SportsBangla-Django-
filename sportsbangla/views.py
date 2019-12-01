from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render

def login_redirect(request):
    return redirect('/account/login')