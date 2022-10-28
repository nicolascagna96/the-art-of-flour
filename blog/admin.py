from django.contrib import admin
from .models import Post, Comment, Recipes, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Comment)


class RecipesAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'recipe_name', 'body', 'ingredients', 'image')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'recipe_name', 'body')
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Recipes)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'body','image')
    search_fields = ('name', 'email')
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(Contact)