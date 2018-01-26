from django.contrib import admin
from .models import Tag, Project, Screenshot

# Register your models here.


class ProjectTag(admin.ModelAdmin):

    filter_horizontal = ('tags',)


admin.site.register(Tag)


class ScreenshotInlineAdmin(admin.TabularInline):

    model = Screenshot


admin.site.register(Project)

admin.site.register(Screenshot)
