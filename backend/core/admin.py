from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(About)
admin.site.register(Chance)
admin.site.register(Coupon)

@admin.register(Fakultet)
class FakultetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_url')
    prepopulated_fields = {'slug': ('name',)}