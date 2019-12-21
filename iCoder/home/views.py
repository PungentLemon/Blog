from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name) < 2 or len(email) < 2 or len(phone) < 2 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, "Your messasge has been successfully sent")
    return render(request, 'home/contact.html')


def search(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(title__icontains=query)
    params = {'allPosts': allPosts}
    return render(request, 'home/search.html', params)
