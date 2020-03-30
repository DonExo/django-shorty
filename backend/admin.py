from django.contrib import admin
from .models import Shortener


class AdminShortener(admin.ModelAdmin):
    list_display = ('short_url', 'original_url', 'times_visited')
    # readonly_fields = ('short_url', )


admin.site.register(Shortener, AdminShortener)