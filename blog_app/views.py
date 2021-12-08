from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import post, comment
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from time import sleep
from django.contrib.auth.decorators import login_required
from .forms import postform, commentform, UserCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from blog_app import forms
# Create your views here.
def index(request):
     posts = post.objects.all().order_by('-update')[:4]
     all_posts = post.objects.all().order_by('-update')[:18]
     context = {
          'posts' : posts,
          'all_posts' : all_posts,
     }
     return render(request, 'base/index.html', context)

@login_required(login_url='Login')
def Profile(request, pk):
     user = User.objects.get(id=pk)
     posts = user.post_set.all()

     context = {
          'user' : user,
          'posts' : posts
     }
     return render(request, 'base/author.html', context)

@login_required(login_url='Login')
def postview(request, pk):
     context = {}
     my_post = post.objects.get(id=pk)
     liked_people = my_post.liked.all()
     posts = post.objects.filter(Topic__icontains = my_post.Topic)
     context = {
               'posts' : posts,
               'my_post' : my_post,
               'liked_people': liked_people
          }
     
     return render(request, 'base/post.html', context)

@login_required(login_url='Login')
def create(request):
     form = postform()
     if request.method == 'POST':
        form = postform(request.POST, request.FILES)
        if form.is_valid():
          new_form = form.save(commit=False)
          new_form.author = request.user
          new_form.save()
          return redirect('home')
     context = {'form': form, 'create' : True}
     return render(request, 'base/room_form.html', context)

@login_required(login_url='Login')
def edit(request, pk):
     posts = post.objects.get(id=pk)
     form = postform(instance=posts)
     if request.method == 'POST':
        form = postform(request.POST, request.FILES, instance=posts)
        if form.is_valid():
          new_form = form.save(commit=False)
          new_form.author = request.user
          new_form.save()
          return redirect('create')
     context = {'form': form, 'create' : True}
     return render(request, 'base/room_form.html', context)
     
def Loginpage(request): 
     if request.user.is_authenticated:
          return redirect('home')
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          try:
               user = User.objects.get(username=username)
          except:
               messages.error(request, 'User does not exist')

          user = authenticate(request, username=username, password=password) 
          if user is not None:
               login(request, user)
               return redirect('home')
     
     context = {'login' : True}
     return render(request, 'base/login.html', context)
     
def logoutpage(request):
     if request.method == 'POST':
          logout(request)
          return redirect('home')
     return render(request, 'base/login.html', {'logout' : True})

@login_required(login_url='Login')
def deletepost(request, pk):
     form = post.objects.get(id=pk)
     try:
          if request.method == 'POST':
               form.delete()
               return redirect('home')
     except:
          return render(request, 'base/delete.html', {'post':form})
     return render(request, 'base/delete.html', {'form' : form, 'create' : True})

def register(request):
     if request.user.is_authenticated:
          return redirect('home')
     form = UserCreateForm()
     if request.method == 'POST':
          form = UserCreateForm(request.POST)
          if form.is_valid():
               user = form.save(commit=False)
               user.username = user.username.lower()
               user.save()
               login(request, user)
               return redirect('home')
     return render(request, 'base/register.html', {'form' : form})
     
@login_required(login_url='Login')
def like_post(request):
     usering = request.user
     if request.method == 'POST':
          post_id = request.POST.get('post_id')
          post_obj = post.objects.get(id=post_id)
          if usering in post_obj.liked.all():
               post_obj.liked.remove(usering)
          else:
               post_obj.liked.add(usering)
     return HttpResponseRedirect(post_id)


