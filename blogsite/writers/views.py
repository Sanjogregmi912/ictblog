from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username =username, password=password,is_superuser=False)
        if user is not None:
            auth.login(request,user)
            return redirect('/writer/dashboard')
        else:
            print(user)
            messages.error(request,"Username or password is wrong")
            return redirect('/writer/login')
    return render(request, 'writers/login.html')

def addstaff(request):
    if request.method == 'POST':
        id = request.POST['id']
        first_name=request.POST['firstname']
        last_name=request.POST["lastname"]
        username=request.POST["username"]
        
        password = request.POST["password"]
      
        user = User.objects.create_user(username=username,password=password,id=id,first_name=first_name,last_name=last_name)
        user.save()
        return redirect('/writer/viewstaff')
    
    return render(request, 'writers/addstaff.html')
    
def viewstaff(request):
    if request.method=="POST":
        page =int(request.POST['page'])
        if('prev' in request.POST):
            page=page-1
        if('next' in request.POST):
            page=page+1
        tempOffSet=page - 1
        offset=tempOffSet*4
        print(offset)
    else:
        offset=0
        page=1
        
    writer =User.objects.raw("select * from auth_user limit 4 offset % s",[offset])
    pageItem = len(writer)    
    return render(request, 'writers/viewstaff.html',{'page':page,'writer':writer,'pageItem':pageItem})
def dashboard(request):
    return render (request,'writers/dashboard.html')