from django.contrib import admin
from .models import question, choice


class choiceInLine(admin.TabularInline):
    model = choice
    extra = 3
    
    
class questionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["questionText"]}),
        ("Date information", {"fields": ["pubDate"], "classes": ["collapse"]}),
    ]
    inlines = [choiceInLine]
    list_display = ["questionText", "pubDate", "wasPublishedRecently"]
    list_filter = ["pubDate"]
    search_fields = ["questionText"]


admin.site.register(question, questionAdmin)

# Register your models here.
