from django.shortcuts import render
from blog.models import BlogsPost
from django.http import HttpResponseRedirect, HttpResponse

from .forms import LoginForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.


def blog_index(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request, 'index.html', {'blog_list':blog_list})   # 返回index.html页面


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'login_error.html')


    else:
        form = LoginForm()
        return render(request, 'login.html',
                      {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def about_view(request):
    return render(request, 'about.html')