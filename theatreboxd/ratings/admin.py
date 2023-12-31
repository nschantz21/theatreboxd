from django.contrib import admin

# Register your models here.
from .models import (
    Agent, Show, Production,
    Performance, Rating, Star,
    Crew, Cast, Venue, Role,
    Character
)

# Admin classes
class CrewAdmin(admin.ModelAdmin):
    list_display = ('show', 'agent', 'role')

class CastAdmin(admin.ModelAdmin):
    list_display = ('agent', 'character', 'swing', 'understudy')

class ProductionAdmin(admin.ModelAdmin):
    ordering = ["show", "start_date"]

class AgentAdmin(admin.ModelAdmin):
    ordering = ["last_name", "first_name", "date_of_birth"]

class RoleAdmin(admin.ModelAdmin):
    ordering = ["name"]

# registry
admin.site.register(Agent, AgentAdmin)
admin.site.register(Show)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(Production, ProductionAdmin)
admin.site.register(Performance)
admin.site.register(Rating)
admin.site.register(Role, RoleAdmin)
admin.site.register(Star)
admin.site.register(Venue)
admin.site.register(Character)
