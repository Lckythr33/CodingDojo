from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'hello/index.html') 


def create_user(request):
    print(request.POST['first_name'])
    print(request.POST['last_name'])
    return redirect("/users")