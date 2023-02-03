from django.forms import ModelForm #creates an html5 form from a model
from .models import Feeding

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ('date', 'meal')