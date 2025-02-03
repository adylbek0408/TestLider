from django.contrib import admin
from .models import (
    Ajy,
    CategoryPackage,
    Package,
    PhotoPackage,
    Combo,
    ArticleOrNews,
    Lesson,
)


@admin.register(Ajy)
class AjyAdmin(admin.ModelAdmin):
    list_display = ("name", "bio")
    search_fields = ("name", "bio")
    list_filter = ("name",)


@admin.register(CategoryPackage)
class CategoryPackageAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0
    fields = ("package", "date", "video_url", "description")
    autocomplete_fields = ["package"]


class ComboInline(admin.StackedInline):
    model = Combo
    extra = 0
    fields = ("package", "combo_choices", "name", "rich", "image", "date")
    autocomplete_fields = ["package"]


class PhotoPackageInline(admin.StackedInline):
    model = PhotoPackage
    extra = 0
    fields = ("package", "image")


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "ajy", "start_tour", "end_tour", "price")
    search_fields = ("name", "description", "category__name", "ajy__name")
    list_filter = ("category", "ajy", "start_tour", "end_tour")
    autocomplete_fields = ["category", "ajy"]
    inlines = [PhotoPackageInline, ComboInline, LessonInline]


@admin.register(ArticleOrNews)
class ArticleOrNewsAdmin(admin.ModelAdmin):
    list_display = ("name", "choices", "date")
    search_fields = ("name", "description")
    list_filter = ("choices", "date")
