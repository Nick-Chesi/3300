from django.contrib import admin
from .models import adminModel
from .models import Portfolio
from .models import Student
# Register your models here.

admin.site.register(adminModel)
admin.site.register(Student)
admin.site.register(Portfolio)