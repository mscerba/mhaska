from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from . models import Category, Post



class PostAdmin(admin.ModelAdmin):

	list_display = ('title', 'update_date', 'category')
	ordering = ('category',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, DraggableMPTTAdmin)


