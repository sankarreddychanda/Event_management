from django.shortcuts import render

# Create your views here

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about-us.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def blog_detail(request):
    return render(request,'blog-details.html')

def schedule(request):
    return render(request,'schedule.html')

def speaker(request):
    return render(request,'speaker.html')

