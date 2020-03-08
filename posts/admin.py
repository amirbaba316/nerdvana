from django.contrib import admin
from .models import Post,Comment,SubComment

class PostAdmin(admin.ModelAdmin):
    list_display=['title','creator','group']
    readonly_fields=['comment_count','likes']

    def comment_count(self,obj,*args,**kwargs):
        objs=obj.comment.all()
        return objs.count()

class CommentAdmin(admin.ModelAdmin):
    list_display=['content','creator','post']
    readonly_fields=['subcomment_count',]

    def subcomment_count(self,obj,*args,**kwargs):
        objs=obj.sub_comment.all()
        return objs.count()



admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(SubComment)
