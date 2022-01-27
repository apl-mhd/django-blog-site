from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.template import context
from . models import Post
from . forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'base/index.html', context)

@login_required(login_url ='index')
def postCreate(request):

    form = PostForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'base/post-create.html', context)


def postUpdate(request, id):

    obj = Post.objects.get(id = id)
    form =  PostForm(instance=obj)
 
    context = {
        'post': obj,
        'form': form,
    }

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = PostForm(request.POST, instance=obj)

            form.save()
            return redirect('index')
        
    return render(request, 'base/post-update.html', context)


def postDelete(request, id):

    post =  Post.objects.get(id = id)
    #post.delete()
    #return redirect('index')

    context = {
        'post': post
    }

    return render(request, 'base/post-delete.html', context)

def postDeleteSuccess(request, id):
    Post.objects.get(id = id).delete()
    return redirect('index')


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        print(username)
        print(password)



        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'base/login.html')


def logoutPage(request):

    logout(request)
    return redirect('login')

def registerPage(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        
        else:
            return redirect('register')

    context = {
        'form': form,
    }

    return render(request, 'base/register.html', context)

    


