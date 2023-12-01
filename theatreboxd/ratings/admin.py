from django.contrib import admin

# Register your models here.
from .models import (
    Agent, Show, Production,
    Performance, Rating, Stars,
    CastCrew, Venue
)

# Admin classes
class CastCrewAdmin(admin.ModelAdmin):
    list_display = ('show', 'agent', 'role')

# registry
admin.site.register(Agent)
admin.site.register(Show)
admin.site.register(CastCrew, CastCrewAdmin)
admin.site.register(Production)
admin.site.register(Performance)
admin.site.register(Rating)
admin.site.register(Stars)
admin.site.register(Venue)
