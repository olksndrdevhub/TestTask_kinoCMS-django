from django.contrib import admin

from .models import Film, News, FilmGallery, FilmShowSession

class ImagesInline(admin.TabularInline):
  model = FilmGallery

class SessionsInline(admin.TabularInline):
    model = FilmShowSession

class FilmAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
        SessionsInline
        ]
    list_display = ['title', 'slug', 'poster', 'show_today', 'show_soon', 'can_sell_ticket', 'show_soon_from_date', 'show_soon_to_date', 'show_now_to_date']
    prepopulated_fields = {'slug': ['title'],
                           
                            }


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Film, FilmAdmin)
admin.site.register(News, NewsAdmin)
