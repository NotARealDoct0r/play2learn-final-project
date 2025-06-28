from django.views.generic import TemplateView

from reviews.models import Review

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review_list"] = Review.objects.filter(featured=True).order_by('-created')
        return context

class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'