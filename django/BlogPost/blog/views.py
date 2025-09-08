from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return render(request, 'base.html')
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'base.html')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in. Please try again...")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out...")
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, "Username already taken. Please choose another one...")
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.success(request, "Email already registered. Please choose another one...")
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    messages.success(request, "User created successfully. Please login...")
                    return redirect('login')
        else:
            messages.success(request, "Passwords do not match. Please try again...")
            return redirect('signup')
    else:
        return render(request, 'signup.html')
    
@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        blog = Blog(title=title, content=content, author=author)
        blog.save()
        messages.success(request, "Blog post created successfully.")
        return redirect('home')
    else:
        return render(request, 'create_blog.html')

@login_required(login_url='login')    
def view_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'view_blogs.html', {'blogs': blogs})

@login_required(login_url='login')
def view_blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'view_blog_detail.html', {'blog': blog})

@login_required(login_url='login')
def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.user != blog.author:
        messages.success(request, "You are not authorized to edit this blog post.")
        return redirect('blogs')
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        messages.success(request, "Blog post updated successfully.")
        return redirect('blog', blog_id=blog.id)
    else:
        return render(request, 'edit_blog.html', {'blog': blog})
    
@login_required(login_url='login')
def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.user != blog.author:
        messages.success(request, "You are not authorized to delete this blog post.")
        return redirect('blogs')
    blog.delete()
    messages.success(request, "Blog post deleted successfully.")
    return redirect('blogs')

@login_required
def profile(request):
    user = request.user
    blogs = Blog.objects.filter(author=user).order_by('-created_at')
    return render(request, 'profile.html', {'user': user, 'blogs': blogs})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST.get('username')
        email = request.POST.get('email')

        user.username = username
        user.email = email
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')
    
    return render(request, 'edit_profile.html', {'user': request.user})

@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('signup')
    return render(request, 'delete_account.html')

