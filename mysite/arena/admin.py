from django.contrib import admin

from .models import *

class QueueInline(admin.TabularInline):
    model = Queue
    #fk_name = "arena_id"

class ArenaAdmin(admin.ModelAdmin):
    fields = ["lower_bound", "upper_bound", "reward_level", "reward_money", "rang"]
    inlines = [QueueInline]


class QueueAdmin(admin.ModelAdmin):
    fields = ["arena_id","toad1","toad2"]

admin.site.register(Arena, ArenaAdmin)
admin.site.register(Queue, QueueAdmin)
