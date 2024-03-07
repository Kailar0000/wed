from django.contrib import admin
from .models import Federation, TypeEvent, ClassEvent, Event, Club, Document, Team


admin.site.register(Federation)
admin.site.register(TypeEvent)
admin.site.register(ClassEvent)
admin.site.register(Event)
admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Document)