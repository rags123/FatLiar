from django.contrib import admin
from site_one.models import Blog


# class BlogAdmin(admin.ModelAdmin):
#     exclude = ['posted']
#     prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog)
# admin.site.register(BlogContent)
