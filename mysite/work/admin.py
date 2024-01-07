from django.contrib import admin

from .models import Work


class WorkAdmin(admin.ModelAdmin):
    fields = ["type_of_work", "reward_score","reward_money"]
    
admin.site.register(Work, WorkAdmin)