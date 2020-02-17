from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime

def index(request):
     return render(request, 'app_ckeiba/index.html')
    
