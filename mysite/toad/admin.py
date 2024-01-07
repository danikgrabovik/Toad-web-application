from django.contrib import admin
from django import forms
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt


from .models import *

class BackpacksInline(admin.TabularInline):
    model = Backpacks
    extra = 3

class FriendsInline(admin.TabularInline):
    model = Friends
    fk_name = "friend1"

class RequestsInline(admin.TabularInline):
    model = Requests
    fk_name = "request_from"

class MyRequestsInline(admin.TabularInline):
    model = Requests
    fk_name = "request_to"


def check_work_adm(modeladmin, request, queryset):
    for obj in queryset:
        obj.check_work()


class ToadAdmin(ExtraButtonsMixin,admin.ModelAdmin):
    
    fields = ["name","money","curr_level","level_progress","health","backpack","last_feed"]
    inlines = [BackpacksInline,FriendsInline,RequestsInline,MyRequestsInline]
    actions = [check_work_adm]
    
    # @button(change_form=True,
    #         html_attrs={'style': 'background-color:#88FF88;color:black'})
    # def refresh(self, request):
    #     self.message_user(request, 'refresh called')
        
    #     # Optional: returns HttpResponse
    #     return HttpResponseRedirectToReferrer(request)
    
    # @button(change_form=True,
    #         html_attrs={'style': 'background-color:#88FF88;color:black'})

        


class WorkToadAdmin(admin.ModelAdmin):
    fields = ["work", "toad","start_time"]

class FriendsAdmin(admin.ModelAdmin):
    fields = ["friend1", "friend2"]

class RequestsAdmin(admin.ModelAdmin):
    fields = ["request_from", "request_to","accepted","ignore"]

class BackpacksAdmin(admin.ModelAdmin):
    fields = ["owner", "product"]

class Arena_requestAdmin(admin.ModelAdmin):
    fields = ["from_toad"]



admin.site.register(Toad, ToadAdmin)
admin.site.register(WorkToad, WorkToadAdmin)
admin.site.register(Friends, FriendsAdmin)
admin.site.register(Requests, RequestsAdmin)
admin.site.register(Backpacks, BackpacksAdmin)
admin.site.register(Arena_request, Arena_requestAdmin)