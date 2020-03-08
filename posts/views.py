from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from .forms import CreatePostForm,CommentPostForm,SubCommentPostForm
from .models import Post,Comment,SubComment
from group.models import Group
from customuser.models import CustomUser
from django.contrib import messages


class CreatePost(View):
    form_class=CreatePostForm
    template_name='create_post.html'
    def get(self,request,pk):
        group=get_object_or_404(Group,pk=pk)
        context={'form':self.form_class(),'group':group}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        group=get_object_or_404(Group,pk=pk)
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            obj=bound_form.save(commit=False)
            obj.creator=request.user.username
            obj.group=group
            obj.save()
            return redirect('detail_post',pk)

        else:
            return render(request,self.template_name,{'form':bound_form,'group':group})

class PostListView(View):
    template_name="post_detail.html"
    def get(self,request):
        post_list=Post.objects.all()
        context={'posts':post_list}
        return render(request,self.template_name,context)


class PostDetailView(View):
    template_name="post_detail.html"
    comment_form_class=CommentPostForm
    subcomment_form_class=SubCommentPostForm
    def get(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        members=[]
        for i in list(post.group.members.all()):
            members.append(i.username)
        context={'members':members,'post':post,'com_form':self.comment_form_class(),'sub_com_form':self.subcomment_form_class()}
        return render(request,self.template_name,context)
    def post(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        context={'post':post,'com_form':self.comment_form_class(),'sub_com_form':self.subcomment_form_class()}
        return render(request,self.template_name,context)


class PostDeleteView(View):
    template_name="post_confirm_delete.html"
    def get(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        context={'post':post}
        return render(request,self.template_name,context)
    def post(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        post.delete()
        messages.success(request,'Post has been deleted')
        return redirect('homepage')


class PostUpdateView(View):
    template_name="update_post.html"
    form_class=CreatePostForm
    def get(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        cont_dict={'title':post.title,'content':post.content}
        bound_form=self.form_class(cont_dict)
        context={'post':post,'form':bound_form}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('detail_post',pk)

class CommentPostView(View):
    com_form_class=CommentPostForm
    sub_com_form_class=SubCommentPostForm
    template_name="post_detail.html"
    def post(self,request,pk):
        bound_form=self.com_form_class(request.POST)
        if bound_form.is_valid():
            post=get_object_or_404(Post,pk=pk)
            obj=bound_form.save(commit=False)
            creator=request.user.username
            obj.photo=get_object_or_404(CustomUser,username=creator).photo
            obj.creator=creator
            obj.post=post
            obj.save()
            return redirect("detail_post",pk)
        else:
            context={'post':post,'com_form':self.com_form_class(),'sub_com_form':self.sub_com_form_class()}
            return render(request,self.template_name,context)
        

class SubCommentPostView(View):
    com_form_class=CommentPostForm
    sub_com_form_class=SubCommentPostForm
    def post(self,request,pk):
        bound_form=self.sub_com_form_class(request.POST)
        if bound_form.is_valid():
            comment=get_object_or_404(Comment,pk=pk)
            obj=bound_form.save(commit=False)
            creator=request.user.username
            obj.photo=get_object_or_404(CustomUser,username=creator).photo
            obj.creator=creator
            obj.comment=comment
            obj.save()
            return redirect("list_group")
        else:
            return redirect("list_group")

class MetaCommentPostView(View):
    com_form_class=CommentPostForm
    sub_com_form_class=SubCommentPostForm
    template_name="post_detail.html"
    def post(self,request,c_pk,s_pk):
        bound_form=self.sub_com_form_class(request.POST)
        if bound_form.is_valid():
            comment=get_object_or_404(Comment,pk=c_pk)
            sub_comment=get_object_or_404(SubComment,pk=s_pk)
            obj=bound_form.save(commit=False)
            creator=request.user.username
            obj.photo=get_object_or_404(CustomUser,username=creator).photo
            obj.creator=creator
            obj.comment=comment
            obj.sub_comment=sub_comment
            obj.save()
            return redirect("list_group")
        else:
            return redirect("list_group")
            
        

