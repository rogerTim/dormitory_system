from django.contrib import admin
from .models import user, dor_arr, dormitory, building, user_answer, question

# Register your models here.

admin.site.register(dormitory)
admin.site.register(building)
admin.site.register(user_answer)
admin.site.register(user)
admin.site.register(dor_arr)
admin.site.register(question)
