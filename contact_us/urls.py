from django.urls import path

from .views import ContactUsView, ContactUsThanksView

app_name = 'contact_us'
urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name='contact_form'),
    path('contact-us/thanks/', ContactUsThanksView.as_view(), name='thanks'),
]