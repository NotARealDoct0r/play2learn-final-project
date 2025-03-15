from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Review

class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'message']

class ReviewDetailView(DetailView):
    model = Review

class ReviewListView(ListView):
    model = Review

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['title', 'message']