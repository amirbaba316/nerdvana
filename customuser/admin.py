from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):

    readonly_fields=['In_groups']

    def In_groups(self,obj,*args,**kwargs):
        objects=obj.members.all()
        groups=[]
        for group in objects:
            groups.append(group.name)

        return groups

admin.site.register(CustomUser,CustomUserAdmin)

    

    
