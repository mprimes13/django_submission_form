from django.forms import ModelForm
from .models import Personal

class SubmissionForm(ModelForm):
    class Meta:
        model  = Personal
        fields = ['name','age','title','hometown']
        required = ['name', 'title']