from django.contrib import admin
from.forms import  SignUPFORM,Loginform
from .models import SignUp,login

class SUadmin(admin.ModelAdmin):
	list_display=["name","createdon","updated","image"]
	model=SignUp
	form=SignUPFORM

admin.site.register(SignUp,SUadmin)


class LoginAdmin(admin.ModelAdmin):
	list_display=["emailog"]
	model=login
	form=Loginform


admin.site.register(login,LoginAdmin)