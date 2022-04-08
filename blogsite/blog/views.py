from django.shortcuts import render,redirect
from django.views import generic
from blog.form import BlogForm
from blog.models import Blog

# Create your views here.
def blogsall(request):
    blog = Blog.objects.filter(status=1).order_by('-created_on')
    return render(request,'blog/blogs.html',{'blog':blog})
def addblog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect('/writer/dashboard')
            except:
                print("failed")
        else:
            form = BlogForm()
            print("invalid ")
    return render(request,'blog/addblog.html')

class PostDetail(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'