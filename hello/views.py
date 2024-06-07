from django.shortcuts import render , redirect
from .forms import DealerForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Dealer


def home(request):
    return HttpResponse("yo")

def showformdata(request):
    if request.method == "GET":
        sf=DealerForm()
        return render(request, 'forms/registration.html', {'form':sf})
    elif request.method == "POST":
        form = DealerForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("hello:dealerurl")
