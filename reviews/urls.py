from django.urls import path

from .views import (ReviewCreateView ,ReviewDetailView, ReviewListView, 
                    ReviewUpdateView)

app_name = 'reviews'
urlpatterns = [
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='update'),
    path('review/create/', ReviewCreateView.as_view(), name='create'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='detail'),
    path('', ReviewListView.as_view(), name='list'),
]