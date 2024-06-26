from django.contrib import admin
from .models import Machine, User, Robot, Process

# Register your models here.

admin.site.register(Machine)
admin.site.register(User)
admin.site.register(Robot)
admin.site.register(Process)
