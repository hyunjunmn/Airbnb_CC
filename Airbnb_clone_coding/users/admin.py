from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.

@admin.register(models.User)#항상 클래스보다 바로 위에 있어야 함
class CustomUserAdmin(UserAdmin):
    
    fieldsets =UserAdmin.fieldsets + (
        (
            "Custom Profile",{
                "fields":(
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
       "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    
    )
    
    list_filter = UserAdmin.list_filter + ("superhost",)


"""class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username","gender","email","language","currency","superhost")
    #user페이지의 list를 보여주는 테이블
    list_filter = ("superhost","language","currency",)
    #filterbox 생성
#@admin.register(models.User)
#admin.site.register(models.User,CustomUserAdmin) 위에것과 같음
"""