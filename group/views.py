from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from .forms import CreateGroupForm
from .models import Group
from customuser.models import CustomUser
from django.contrib import messages


class CreateGroup(View):
    form_class=CreateGroupForm
    template_name='create_group.html'
    def get(self,request):
        context={'form':self.form_class()}
        return render(request,self.template_name,context)

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            obj=bound_form.save(commit=False)
            obj.creator=request.user.username
            obj.save()
            return render(request,self.template_name,{'form':bound_form})

        else:
            return render(request,self.template_name,{'form':bound_form})

class GroupListView(View):
    template_name="group_list.html"
    def get(self,request):
        group_list=Group.objects.all()
        context={'groups':group_list}
        return render(request,self.template_name,context)


class GroupDetailView(View):
    template_name="group_detail.html"
    def get(self,request,pk):
        group=get_object_or_404(Group,pk=pk)
        members=[]
        for i in list(group.members.all()):
            members.append(i.username)
        context={'members':members,'group':group}
        return render(request,self.template_name,context)


class FollowGroupView(View):
    template_name="group_detail.html"
    def get(self,request,pk):
        group=get_object_or_404(Group,pk=pk)
        username=request.user.username
        user=get_object_or_404(CustomUser,username=username)
        group.members.add(user)
        context={'group':group}
        return render(request,self.template_name,context)

class GroupDeleteView(View):
    template_name="confirm_delete.html"
    def get(self,request,pk):
        group=get_object_or_404(Group,pk=pk)
        context={'group':group}
        return render(request,self.template_name,context)
    def post(self,request,pk):
        group=get_object_or_404(Group,pk=pk)
        group.delete()
        messages.success(request,'Group has been deleted')
        return redirect('list_group')


class GroupUpdateView(View):
    template_name="update_group.html"
    form_class=CreateGroupForm
    def get(self,request,pk):
        group=get_object_or_404(Group,pk=pk)
        cont_dict={'name':group.name,'description':group.description}
        bound_form=self.form_class(cont_dict)
        context={'group':group,'form':bound_form}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        group=get_object_or_404(Group,pk=pk)
        group.name=request.POST['name']
        group.description=request.POST['description']
        group.save()
        return redirect('detail_group',pk)
        





        

