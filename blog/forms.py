from django import forms

from .models import PostModel

class PostFrom(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
        attrs={
            'class':'w-full px-0 text-sm text-gray-900 bg-white border-0 focus:ring-0',
            'rows':2,
            'placeholder':'Write a comment...'
            }
        ),
        required=True,
    )
    
    image = forms.ImageField(
        required=False,
    )
    
    class Meta:
        model = PostModel
        fields = ['content', 'image']