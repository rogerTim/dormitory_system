from django.contrib import admin
from .models import User, DorArrange, Dormitory, Building, User_answer, Question

# Register your models here.

admin.site.register(Dormitory)
admin.site.register(Building)
admin.site.register(User_answer)
admin.site.register(User)
admin.site.register(DorArrange)
admin.site.register(Question)
