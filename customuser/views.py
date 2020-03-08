from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import CreateUserForm,AuthenticateForm
from django.contrib import auth,messages
from .models import CustomUser
from group.models import Group

class CreateUserView(View):
    form_class=CreateUserForm
    def get(self,request):
        context={'form':self.form_class()}
        return render(request,"user/create_user.html",context)

    def post(self,request):
        bound_form=self.form_class(request.POST)
        context={'form':self.form_class()}
        if bound_form.is_valid():
            user=bound_form.save(commit=False)
            user.set_password(user.password)
            if 'photo' in request.FILES:
                user.photo=request.FILES['photo']
                user.save()
            return render(request,"user/create_user.html",context)
        else:
            return render(request,"user/create_user.html",{'form':bound_form})

class HomePageView(View):
    def get(self,request):
        template_name="user/feed.html"
        group_list=Group.objects.all()
        username=request.user.username
        user=CustomUser.objects.all().filter(username=username).first()
        groups=user.members.all()
        posts=[]
        for group in groups:
            posts+=(list(group.posts.all().order_by('-published_date')))
        
        context={'posts':posts,'groups':group_list,'user':user}
        return render(request,template_name,context)

class LoginView(View):
    form_class=AuthenticateForm
    def get(self,request):
        return render(request,'user/login.html',{'form':self.form_class()})

    def post(self,request):
        username=self.request.POST["username"]
        password=self.request.POST["password"]

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are logged in now')
            return redirect('login')
        else:
            messages.error(request,'invalid credintials')
            return redirect('login')

class LogoutView(View):
    def get(self,request):
        auth.logout(request)
        messages.success(request,"you are logged out now")
        return redirect("login")




