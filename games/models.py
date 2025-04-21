from django.conf import settings
from django.db import models

class GameScore(models.Model):
    GAME_TYPE_CHOICES = [
        ('anagram', 'Anagram Hunt'),
        ('math', 'Math Facts'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    game_type = models.CharField(max_length=20, choices=GAME_TYPE_CHOICES)
    score = models.IntegerField()
    word_length = models.IntegerField(blank=True, null=True)  # only for anagram
    operation = models.CharField(max_length=10, blank=True, null=True)  # only for math
    max_number = models.IntegerField(blank=True, null=True)  # only for math
    finished_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - {self.game_type} - {self.score}"
