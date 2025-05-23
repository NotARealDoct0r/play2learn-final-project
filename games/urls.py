from django.urls import path
from games.views import (
    MathFactsView,
    MathFactsTrackingView,
    AnagramHuntView,
    AnagramHuntTrackingView,
    record_score,
)

app_name = 'games'

urlpatterns = [
    path("api/record-score/", record_score, name="record_score"),
    path("math-facts/", MathFactsView.as_view(), name="math-facts"),
    path("math-facts-tracking/", MathFactsTrackingView.as_view(), name="math-facts-tracking"),
    path("anagram-hunt/", AnagramHuntView.as_view(), name="anagram-hunt"),
    path("anagram-hunt-tracking/", AnagramHuntTrackingView.as_view(), name="anagram-hunt-tracking"),
]
