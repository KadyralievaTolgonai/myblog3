from django.contrib import admin
from .models import *
class PostImageInline(admin.TabularInline):
    model=PostImage
    max_num=10
    min_num=1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields='__all__'
    inlines=[PostImageInline,]

# Register your models here.
admin.site.register(Category)


