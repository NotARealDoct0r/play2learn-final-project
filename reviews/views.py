from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView,DetailView, ListView, UpdateView
)

from .models import Review

class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'message']

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:list')

class ReviewDetailView(DetailView):
    model = Review

class ReviewListView(ListView):
    model = Review

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['title', 'message']