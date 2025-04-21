import json

from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import GameScore

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class AnagramHuntTrackingView(LoginRequiredMixin, TemplateView):
    template_name = "anagram-hunt-tracking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["history"] = GameScore.objects.filter(user=user, game_type="anagram").order_by('-finished_at')[:10]
        context["leaderboard"] = GameScore.objects.filter(game_type="anagram").order_by('-score')[:3]
        return context

class MathFactsTrackingView(LoginRequiredMixin, TemplateView):
    template_name = "math-facts-tracking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["history"] = GameScore.objects.filter(user=user, game_type="math").order_by('-finished_at')[:10]
        context["leaderboard"] = GameScore.objects.filter(game_type="math").order_by('-score')[:3]
        return context

# API view for recording scores
@csrf_protect
def record_score(request):
    if request.method == "POST":

        try:
            data = json.loads(request.body)
            user = request.user if request.user.is_authenticated else None
            score = data.get("score", 0)
            settings = data.get("game_settings", {})
            word_length = settings.get("word_length", 0)
            operation = settings.get("operation", "Addition")
            max_number = settings.get("max_number", 1)
            game_type = data.get("game_type", "anagram")  # Default to 'anagram'

            if score is None or word_length is None:
                return JsonResponse({'error': 'Missing score or word_length'}, status=400)

            # Save the score in the database
            game_score = GameScore.objects.create(
                user=user,
                score=score,
                word_length=word_length,
                operation=operation,
                max_number=max_number,
                game_type=game_type,
            )

            return JsonResponse({"message": "Score recorded", "score_id": game_score.id}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=405)