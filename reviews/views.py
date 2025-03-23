from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView,DetailView, ListView, UpdateView
)

from .forms import ReviewForm
from .models import Review

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:list')

class ReviewDetailView(DetailView):
    model = Review

class ReviewListView(ListView):
    model = Review

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm