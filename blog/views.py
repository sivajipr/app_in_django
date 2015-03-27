
# Create your views here.
#views.py
from blog.forms import *
from blog.admin import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )

def entry(request):
    return render_to_response(
    'entry.html',
        )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
def showblogs(request):
    user=request.user
    blogs=Blog.objects.filter(title=user)
    return render_to_response('allblogs.html',{ 'user': request.user, 'blog': blogs })
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )

@csrf_protect
def write_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = Blog(title=request.user, body=form.cleaned_data['blog_text'])
            blog.save()

            # print ''.join(blog)
            # print type(''.join(blog))
            return HttpResponseRedirect('/register/entry/')
    else:
        form = BlogForm()
        variables = RequestContext(request, {
            'form': form
            })
        return render_to_response(
        'home.html',
        variables,
        )
