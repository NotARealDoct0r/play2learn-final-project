from django.urls import path

from .views import ReviewDetailView, ReviewListView

app_name = 'reviews'
urlpatterns = [
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='detail'),
    path('', ReviewListView.as_view(), name='list'),
]