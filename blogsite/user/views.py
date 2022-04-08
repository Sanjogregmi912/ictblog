from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib import messages
from django.views import generic
from blog.models import Blog
# Create your views here.
def login(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        is_superuser = 1
        user = auth.authenticate(username =username, password=password,is_superuser=is_superuser)
        if user is not None:
            print("valid")
            auth.login(request,user)
            return redirect('/user/dashboard')
        else:
            messages.error(request,"Username or password is wrong")
            return redirect('/user/login')
    return render(request,'admin/login.html')
def dashboard(request):
    return render(request,'admin/dashboard.html')
def allblog(request):
    blog = Blog.objects.filter(status=1).order_by('-created_on')
    return render(request,'blog/blogadmin.html',{'blog':blog})
class PostDetail(generic.DetailView):
    model = Blog
    template_name = 'blog/blog-detailadmin.html'