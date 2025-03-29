from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class AnagramHuntTrackingView(TemplateView):
    template_name = "anagram-hunt-tracking.html"

class MathFactsTrackingView(TemplateView):
    template_name = "math-facts-tracking.html"