from django.views.generic import DetailView, ListView

from .models import Review

class ReviewDetailView(DetailView):
    model = Review

class ReviewListView(ListView):
    model = Review