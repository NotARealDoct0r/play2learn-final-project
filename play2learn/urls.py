from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('users.urls')),
    path('account/', include('allauth.urls')),
    path('reviews/', include('reviews.urls')),
    path('contact-us/', include('contact_us.urls')),
    path('', include('games.urls')),
    path('', include('pages.urls')),
]
