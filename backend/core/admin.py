from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.register(User)
admin.site.register(About)
admin.site.register(Chance)
admin.site.register(Coupon)
admin.site.unregister(Group)
# admin.site.unregister(User_1)

@admin.register(Fakultet)
class FakultetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_url')
    prepopulated_fields = {'slug': ('name',)}