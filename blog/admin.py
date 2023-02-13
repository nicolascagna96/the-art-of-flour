from django.contrib import admin
from .models import Post, Comment, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'body', 'image')
    search_fields = ('name', 'email')
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(approved=True)
