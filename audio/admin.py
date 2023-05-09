from django.contrib import admin
from audio.models import Category, AudioBooks, Chapters
from django.utils.html import format_html




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_date", "updated_date")
    
@admin.register(AudioBooks)
class AudioBooksAdmin(admin.ModelAdmin):
    list_display = ("book_name", "book_author", "publication", "speaker", "publish_date", "cover_album")

    def cover_album(slef, obj):
        return format_html('<img src="{0}" width="auto" height="50px">'.format(obj.album.url))
    
@admin.register(Chapters)
class ChaptersAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "created_at","audio_file","chapter_album")

    def chapter_album(slef, obj):
        return format_html('<img src="{0}" width="auto" height="50px">'.format(obj.album.url))
