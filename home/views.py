from django.shortcuts import render,redirect
from .forms import add_friend_form,add_gallery_form
from .models import Friends,Gallery


# Create your views here.

def index(request):
    return render(request,'index.html')

def admin_page(request):

    return render(request,'admin.html')

def add_friend_page(request):
    if request.method == 'POST':
        form = add_friend_form(request.POST or None,request.FILES or None)
        if form.is_valid():
            form = form.save()
            return redirect('view_friends')
    else:
        form = add_friend_form()
    return render(request,'add_friend.html',{'form':form})

def view_friends(request):
    friends = Friends.objects.all()
    return render(request,'view_friends.html',{'friends':friends})

def edit_friend(request,pk):
    user = Friends.objects.get(pk=pk)

    if request.method == 'POST':
        form = add_friend_form(request.POST or None,request.FILES or None,instance=user)
        if form.is_valid():
            form = form.save()
            return redirect('view_friends')
    else:
        form = add_friend_form(instance = user)
    return render(request,'edit_friend.html',{'form':form})
    

def delete_friend(request,pk):
    user = Friends.objects.get(pk=pk)
    user.delete()
    return redirect('view_friends')

def friend_cell(request):
    friends = Friends.objects.all()
    return render(request,'friend_cell.html',{'friends':friends})

def admin_login(request):
    return render(request,'admin_login.html')

def login(request):
    message = ''
    email = request.POST['username']
    password = request.POST['password']
    
    if email == 'chandanmanna48@gmail.com' and password == 'raju5678':
        messages = 'Logged In Successfully '
        return render(request,'admin.html',{'messages':messages})
    else:
        messages = 'Invalid Email or Password , Try Again ..'
        return render(request,'admin_login.html',{'messages':messages})

def add_gallery(request):
    if request.method == 'POST':
        form = add_gallery_form(request.POST or None,request.FILES or None)
        if form.is_valid():
            form = form.save()
            return redirect('view_gallery')
    else:
        form = add_gallery_form()
    return render(request,'add_gallery.html',{'form':form})


def view_gallery(request):
    images = Gallery.objects.all()
    return render(request,'view_gallery.html',{'images':images})

def gallery(request):
    images = Gallery.objects.all()
    return render(request,'gallery.html',{'images':images})

def delete_image(request,pk):
    image = Gallery.objects.get(pk=pk)
    image.delete()
    return redirect('view_gallery')

