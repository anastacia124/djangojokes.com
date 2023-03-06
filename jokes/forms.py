from django.forms import ModelForm, Textarea

from .models import Joke

class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['question']
        widgets = {
            'question': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            ),
            'answer': Textarea(
                attrs={'cols': 80, 'rows': 2, 'placeholder': ' Add a Review!'}
            )
        }
        help_texts = {
    'question': 'Add a nice review please.',
    'tags': 'Use Ctrl-click to select multiple tags.'
}