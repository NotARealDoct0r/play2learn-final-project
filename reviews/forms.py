from django.forms import ModelForm, Textarea

from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'message']
        widgets = {
            'title': Textarea(
                attrs={'cols': 80, 'rows': 2, 'autofocus': True}
            ),
            'message': Textarea(
                attrs={'cols': 80, 'rows': 3, 'placeholder': 'Share your thoughts!'}
            )
        }
        help_texts = {
            'title': 'No profanity please.'
        }