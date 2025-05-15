from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        content = request.POST.get('content', '').strip()

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly.")
        else:
            new_contact = Contact(name=name, email=email, phone=phone, content=content)
            new_contact.save()
            messages.success(request, 'Your message has been submitted!')
            print(name, phone, email, content)
            return redirect('contact')  # Redirect to the same page to show the message

    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(title_icontains=quert)
    context =  {'allPosts': allPosts}
    
    return render(request, 'home/search.html',context)