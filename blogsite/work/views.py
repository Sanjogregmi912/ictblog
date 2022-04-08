from django.shortcuts import render

# Create your views here.
def work_with_us(request):
    return render(request,'work/work_with_us.html')