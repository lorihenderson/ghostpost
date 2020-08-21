from django import forms
from homepage.models import BoastRoast

class PostForm(forms.ModelForm):
    class Meta:
        model = BoastRoast
        fields = ["choices", "user_input"]
