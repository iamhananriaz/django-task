from django.shortcuts import render , redirect
from .forms import DealerForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import BlogPost, Dealer


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

def blog_post_view(request, post_id):
    try:
        post = get_object_or_404(BlogPost, id=post_id)
    except Http404:
        return HttpResponse('Blog post not found', status=404)
    except Exception as e:
        return HttpResponse(f'An unexpected error occurred: {e}', status=500)
    return render(request, 'blog_post.html', {'post': post})

def blog_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'blogs.html', {'posts': posts})
