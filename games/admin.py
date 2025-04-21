from django.contrib import admin
from .models import GameScore

@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'word_length', 'finished_at')
    list_filter = ('user', 'word_length', 'finished_at')
    search_fields = ('user__username',)
