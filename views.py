from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def create(request):
    return render(request,'form.html')
