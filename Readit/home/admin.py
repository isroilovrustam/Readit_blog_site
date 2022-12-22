from django.contrib import admin
from .models import Home, Article_home, About_home, Contact_home, Single_home
# Register your models here.


admin.site.register(Home)
admin.site.register(Article_home)
admin.site.register(About_home)
admin.site.register(Contact_home)
admin.site.register(Single_home)