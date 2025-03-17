import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from users.utils.email import send_email

from .forms import ContactUsForm

class ContactUsView(FormView):
    template_name = 'contact_us/contact_form.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('contact_us:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'injunchon@gmail.com'
        subject = 'Contact Us Form Submitted'
        content = f'''<p>Hey Administrator!</p>
            <p>Contact Us Form received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ContactUsThanksView(TemplateView):
    template_name = 'contact_us/thanks.html'