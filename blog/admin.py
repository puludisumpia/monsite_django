from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Contact, Subscribe


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ("title", "author", "status", "date",)
    list_filter = ("date", "status",)
    search_fields = ("title", "author",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date",)
    list_filter = ("date",)


@admin.register(Subscribe)
class PostAdmin(admin.ModelAdmin):
    list_display = ("email",)
